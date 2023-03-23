#!/usr/bin/python3
"""Module containing Notification class for representing a team invite"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean, Text, Enum
from sqlalchemy.orm import relationship

class TeamInvite(BaseModel, Base):
    """Class representing a team invite object.

    Attributes:
        __tablename__ (str): The name of the table in the database where team invite objects are stored.
        sender_id (sqlalchemy.Column): The ID of the User object that sent the notification. This ID is a foreign key
            referencing the "id" column in the "users" table.
        receiver_id (sqlalchemy.Column): The ID of the User object that received the notification. This ID is a foreign key
            referencing the "id" column in the "users" table.
        team_id (sqlalchemy.Column): The ID of the Team object that the receiver User is requested to join. This ID is a foreign key
            referencing the "id" column in the "teams" table.
        status (sqlalchemy.Column): A boolean indicating whether the notification has been read by the receiver. The default value is False.
        message (sqlalchemy.Column): The content of the notification. This can be any text up to the maximum allowed length for a Text field.
    """
    __tablename__ = "team_invitations"
    sender_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    receiver_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    team_id = Column(String(60), ForeignKey("teams.id"), nullable=False)
    status = Column(Enum('pending', 'accepted', 'declined', 'seen', name='team_invite_status'), default='pending')
    message = Column(Text)

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])
    team = relationship("Team", foreign_keys=[team_id])
