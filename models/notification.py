#!/usr/bin/python3
"""Notification representation"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship

class Notification(BaseModel, Base):
    """Notification Representation"""
    __tablename__ = "notification"
    sender_id = Column(String(60), ForeignKey("teams.id"), nullable=False)
    receiver_id = Column(String(60), ForeignKey("teams.id"), nullable=False)
    status = Column(Boolean, default=False)
    message = Column(Text)
    #sender = relationship("Team", foreign_keys=[sender_id])
    #receiver = relationship("Team", foreign_keys=[receiver_id])
