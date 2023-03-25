"""
Class representing an invite connection between two teams.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Boolean, Text, Enum
from sqlalchemy.orm import relationship

class GameInvite(BaseModel, Base):
    """
    Attributes:
    __tablename__ (str): The name of the table in the database where GameInvite objects are stored.
    sender_team_id (sqlalchemy.Column): The ID of the first team in the connection. It is a foreign key to the teams table.
    receiver_team (sqlalchemy.Column): The ID of the second team in the connection. It is a foreign key to the teams table.
    game_date (sqlalchemy.Column): The date of the game, if applicable.
    accepted (sqlalchemy.Column): A boolean flag indicating whether the connection has been accepted.
    sender_team (sqlalchemy.orm.relationship): Relationship between GameInvite and Team objects for the first team in the connection.
        This relationship defines a back reference from Team objects to their parent GameInvite object.
    receiver_team (sqlalchemy.orm.relationship): Relationship between GameInvite and Team objects for the second team in the connection.
        This relationship defines a back reference from Team objects to their parent GameInvite object.
    """
    __tablename__ = "game_invitations"
    sender_team_id = Column(String(60), ForeignKey("teams.id"), nullable=False)
    receiver_team_id = Column(String(60), ForeignKey("teams.id"), nullable=False)
    game_date = Column(DateTime)
    status = Column(Enum('pending', 'accepted', 'declined', 'seen', name='game_invite_status'), default='pending')
    message = Column(Text)

    sender_team = relationship("Team", foreign_keys=[sender_team_id])
    receiver_team = relationship("Team", foreign_keys=[receiver_team_id])