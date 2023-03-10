#!/usr/bin/python3
"""TeamConnection representation"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship

class TeamConnection(BaseModel, Base):
    """TeamConnection Representation"""
    __tablename__ = "team_connection"
    team_one_id = Column(String(60), ForeignKey("teams.id"), nullable=False)
    team_two_id = Column(String(60), ForeignKey("teams.id"), nullable=False)
    game_date = Column(DateTime)
    is_completed = Column(Boolean, default=False)
    team_one_score = Column(Integer)
    team_two_score = Column(Integer)

    team_one = relationship("Team", foreign_keys=[team_one_id])
    team_two = relationship("Team", foreign_keys=[team_two_id])
