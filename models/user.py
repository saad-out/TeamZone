#!/usr/bin/python3
"""User representation"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """User Representation"""
    __tablename__ = "users"
    name = Column(String(128), nullable=False)
    username = Column(String(128), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    image = Column(String(128), default='user_default.jpg')
    #bio = Column(Text)
    teams = relationship("Team", secondary="team_membership", overlaps='players')
    
    @property
    def leading_teams(self):
        """Get teams where a user is a leader"""
        teams = []
        for team in self.teams:
            if team.leader_id == self.id:
                teams.append(team)
        
        return (teams)

    @property
    def notifications(self):
        """Get notification for the user based on the teams the user is a leader"""
        notifications = []
        for team in self.leading_teams:
            for notification in team.notifications:
                if notification.status is False:
                    notifications.append(notification)
        return notifications
