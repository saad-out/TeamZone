"""Module defining the User class"""
from flask_login import UserMixin
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship

class User(UserMixin, BaseModel, Base):
    """Attributes:
    __tablename__ (str): The name of the table in the database where User objects are stored.
    name (sqlalchemy.Column): The name of the user. Max length is 128 characters.
    username (sqlalchemy.Column): The username of the user. Max length is 128 characters. Must be unique.
    email (sqlalchemy.Column): The email of the user. Max length is 128 characters. Must be unique.
    password (sqlalchemy.Column): The password of the user. Max length is 128 characters.
    image (sqlalchemy.Column): The image file name of the user. Max length is 128 characters. Default value is "user_default.jpg".
    teams (sqlalchemy.orm.relationship): Relationship between User and Team objects.
        This relationship defines the many-to-many relationship between User and Team objects, which is implemented
        through the "team_membership" table in the database. This relationship also defines the back reference
        from Team objects to their associated User objects.
    leading_teams (property): A property that returns a list of Team objects where the user is the leader.
    notifications (property): A property that returns a list of Notification objects where the user is the leader
        of the associated Team objects and the notification status is "False".
    """
    __tablename__ = "users"
    name = Column(String(128), nullable=False)
    username = Column(String(128), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    image = Column(String(128), default='user_default.jpg')
    teams = relationship("Team", secondary="team_membership", overlaps='players')
    
    @property
    def leading_teams(self):
        """Get teams where a user is a leader"""
        teams = []
        for team in self.teams:
            if team.leader_id == self.id:
                teams.append(team)
        
        return (teams)