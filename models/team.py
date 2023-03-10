#!/usr/bin/python3
"""Team representation"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text, Table
from sqlalchemy.orm import relationship

team_membership = Table('team_membership', Base.metadata,
                        Column("team_id", String(60), ForeignKey("teams.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
                        Column("user_id", String(60), ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
                        )

class Team(BaseModel, Base):
    """Team Representation"""
    __tablename__ = "teams"
    name = Column(String(128), nullable=False)
    bio = Column(Text)
    image = Column(String(128), default='team_default.jpg')
    sport_id = Column(String(60), ForeignKey("sports.id"), nullable=False)
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    leader_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    players = relationship("User", secondary="team_membership", viewonly=False)
    notifications = relationship("Notification", backref="team", foreign_keys="[Notification.receiver_id]", cascade="all, delete, delete-orphan")
    
    leader = relationship("User", foreign_keys=[leader_id])
