#!/usr/bin/python3
"""City representation"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """City Representation"""
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    country_id = Column(String(60), ForeignKey("countries.id"), nullable=False)
    teams = relationship("Team", backref="city", cascade="all, delete, delete-orphan")
