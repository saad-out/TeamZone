#!/usr/bin/python3
"""Module containing Team class for representing a team"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text, Table
from sqlalchemy.orm import relationship

time = "%Y-%m-%dT%H:%M:%S.%f"

team_membership = Table('team_membership', Base.metadata,
                        Column("team_id", String(60), ForeignKey("teams.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
                        Column("user_id", String(60), ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
                        )

class Team(BaseModel, Base):
    """Class representing a Team object.

    Attributes:
        __tablename__ (str): The name of the table in the database where Team objects are stored.
        name (sqlalchemy.Column): The name of the team. This field is required and cannot be empty.
        bio (sqlalchemy.Column): A text description of the team. This field can be empty.
        image (sqlalchemy.Column): The name of an image file representing the team. The default value is 'team_default.jpg'.
        sport_id (sqlalchemy.Column): The ID of the Sport object associated with the team. This ID is a foreign key referencing
            the "id" column in the "sports" table.
        city_id (sqlalchemy.Column): The ID of the City object associated with the team. This ID is a foreign key referencing
            the "id" column in the "cities" table.
        leader_id (sqlalchemy.Column): The ID of the User object who is the leader of the team. This ID is a foreign key referencing
            the "id" column in the "users" table.
        players (sqlalchemy.orm.relationship): A many-to-many relationship between Team and User objects, defined by the
            "team_membership" table.
        notifications (sqlalchemy.orm.relationship): A one-to-many relationship between Team and Notification objects, where
            the team is the receiver of the notifications.
        leader (sqlalchemy.orm.relationship): A one-to-one relationship between Team and User objects, where the user is the
            leader of the team.
    """
    __tablename__ = "teams"
    name = Column(String(128), nullable=False)
    bio = Column(Text)
    image = Column(String(128), default='team_default.jpg')
    sport_id = Column(String(60), ForeignKey("sports.id"), nullable=False)
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    leader_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    players = relationship("User", secondary="team_membership", viewonly=False)
    
    leader = relationship("User", foreign_keys=[leader_id])
    

    def to_dict(self):
        """Returns a dictionary of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        for key in ["_sa_instance_state", "country", "cities", "teams", "players",
                    "notifications", "team_one", "team_two"]:
            if key in new_dict:
                del new_dict[key]

        new_dict["__class__"] = self.__class__.__name__
        new_dict["city"] = self.city.name
        new_dict["country"] = self.city.country.name
        new_dict["sport"] = self.sport.name
        new_dict["leader"] = self.leader.name
        
        return new_dict
