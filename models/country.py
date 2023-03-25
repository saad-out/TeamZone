"""Module containing Country class for representing a country"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Country(BaseModel, Base):
    """Class representing a Country object.

    Attributes:
        __tablename__ (str): The name of the table in the database where Country objects are stored.
        name (sqlalchemy.Column): The name of the country. Max length is 128 characters.
        cities (sqlalchemy.orm.relationship): Relationship between Country and City objects.
            This relationship defines the back reference from City objects to their parent Country object.
            This relationship also defines a cascade behavior, where all related City objects will be deleted
            if their parent Country object is deleted (using "delete" or "delete-orphan" options).
    """
    __tablename__ = "countries"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="country", cascade="all, delete, delete-orphan")
