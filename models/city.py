#!/usr/bin/python3
"""Module containing City class for representing a city"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """Class representing a City object.

    Attributes:
        __tablename__ (str): The name of the table in the database where City objects are stored.
        name (sqlalchemy.Column): The name of the city. Max length is 128 characters.
        country_id (sqlalchemy.Column): The ID of the country that the city belongs to. Max length is 60 characters.
        teams (sqlalchemy.orm.relationship): Relationship between City and Team objects.
            This relationship defines the back reference from Team objects to their parent City object.
            This relationship also defines a cascade behavior, where all related Team objects will be deleted
            if their parent City object is deleted (using "delete" or "delete-orphan" options).
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    country_id = Column(String(60), ForeignKey("countries.id"), nullable=False)
    teams = relationship("Team", backref="city", cascade="all, delete, delete-orphan")
