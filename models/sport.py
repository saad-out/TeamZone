#!/usr/bin/python3
"""Sport representation"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Sport(BaseModel, Base):
    """Sport Representation"""
    __tablename__ = "sports"
    name = Column(String(128), nullable=False)
    teams = relationship("Team", backref="sport", cascade="all, delete, delete-orphan")
