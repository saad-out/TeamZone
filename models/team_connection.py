#!/usr/bin/python3
"""
Class representing a connection between two teams.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship

class TeamConnection(BaseModel, Base):
    """
    Attributes:
    __tablename__ (str): The name of the table in the database where TeamConnection objects are stored.
    team_one_id (sqlalchemy.Column): The ID of the first team in the connection. It is a foreign key to the teams table.
    team_two_id (sqlalchemy.Column): The ID of the second team in the connection. It is a foreign key to the teams table.
    game_date (sqlalchemy.Column): The date of the game, if applicable.
    is_completed (sqlalchemy.Column): A boolean flag indicating whether the connection has been completed.
    team_one_score (sqlalchemy.Column): The score of the first team, if applicable.
    team_two_score (sqlalchemy.Column): The score of the second team, if applicable.
    team_one (sqlalchemy.orm.relationship): Relationship between TeamConnection and Team objects for the first team in the connection.
        This relationship defines a back reference from Team objects to their parent TeamConnection object.
    team_two (sqlalchemy.orm.relationship): Relationship between TeamConnection and Team objects for the second team in the connection.
        This relationship defines a back reference from Team objects to their parent TeamConnection object.
    """
    __tablename__ = "team_connection"
    team_one_id = Column(String(60), ForeignKey("teams.id"), nullable=False)
    team_two_id = Column(String(60), ForeignKey("teams.id"), nullable=False)
    game_date = Column(DateTime)
    is_completed = Column(Boolean, default=False)
    team_one_score = Column(Integer)
    team_two_score = Column(Integer)

    team_one = relationship("Team", foreign_keys=[team_one_id])
    team_two = relationship("Team", foreign_keys=[team_two_id])
