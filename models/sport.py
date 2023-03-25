"""Module containing Sport class for representing a sport"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Sport(BaseModel, Base):
    """Class representing a Sport object.

    Attributes:
        __tablename__ (str): The name of the table in the database where Sport objects are stored.
        name (sqlalchemy.Column): The name of the sport. Max length is 128 characters.
        teams (sqlalchemy.orm.relationship): Relationship between Sport and Team objects.
            This relationship defines the back reference from Team objects to their parent Sport object.
            This relationship also defines a cascade behavior, where all related Team objects will be deleted
            if their parent Sport object is deleted (using "delete" or "delete-orphan" options).
    """
    __tablename__ = "sports"
    name = Column(String(128), nullable=False)
    teams = relationship("Team", backref="sport", cascade="all, delete, delete-orphan")
