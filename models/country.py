#!/usr/bin/python3
"""Country representation"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Country(BaseModel, Base):
    """Country Representation"""
    __tablename__ = "countries"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="country", cascade="all, delete, delete-orphan")
