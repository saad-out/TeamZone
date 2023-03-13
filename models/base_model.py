#!/usr/bin/python3
"""
BaseModel representation.

This class represents the base model class from which other classes will inherit from.
"""

from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()

class BaseModel:
    """
    Attributes:
        id (sqlalchemy.Column): The ID of the object. It's a primary key with a max length of 60 characters.
        created_at (sqlalchemy.Column): The date and time the object was created. Default value is the current date and time.
        updated_at (sqlalchemy.Column): The date and time the object was last updated. Default value is the current date and time.

    Methods:
        init(self, *args, **kwargs): Initializes the base model class.
        str(self): Returns a string representation of the object.
        to_dict(self): Returns a dictionary representation of the object.
        save(self): Saves the object to the database.
        delete(self): Deletes the object from the database.

    """
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.now()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation"""
        obj_dict = self.__dict__
        for key in ["_sa_instance_state", "cities", "teams", "players",
                    "notifications", "team_one", "team_two"]:
            if key in obj_dict:
                del obj_dict[key]
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, obj_dict)

    def to_dict(self):
        """Returns a dictionary of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        for key in ["_sa_instance_state", "cities", "teams", "players",
                    "notifications", "team_one", "team_two"]:
            if key in new_dict:
                del new_dict[key]

        new_dict["__class__"] = self.__class__.__name__

        return new_dict

    def save(self):
        """Update the object"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """delete the object from the database"""
        models.storage.delete(self)
