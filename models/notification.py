#!/usr/bin/python3
"""Module containing Notification class for representing a notification"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship

class Notification(BaseModel, Base):
    """Class representing a Notification object.

    Attributes:
        __tablename__ (str): The name of the table in the database where Notification objects are stored.
        sender_id (sqlalchemy.Column): The ID of the Team object that sent the notification. This ID is a foreign key
            referencing the "id" column in the "teams" table.
        receiver_id (sqlalchemy.Column): The ID of the Team object that received the notification. This ID is a foreign key
            referencing the "id" column in the "teams" table.
        status (sqlalchemy.Column): A boolean indicating whether the notification has been read by the receiver. The default value is False.
        message (sqlalchemy.Column): The content of the notification. This can be any text up to the maximum allowed length for a Text field.
    """
    __tablename__ = "notification"
    sender_id = Column(String(60), ForeignKey("teams.id"), nullable=False)
    receiver_id = Column(String(60), ForeignKey("teams.id"), nullable=False)
    status = Column(Boolean, default=False)
    message = Column(Text)
    #sender = relationship("Team", foreign_keys=[sender_id])
    #receiver = relationship("Team", foreign_keys=[receiver_id])
