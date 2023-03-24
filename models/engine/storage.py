"""
Storage representation.

This class represents the storage class which provides methods to interact with
the database.
"""

from models.base_model import Base, BaseModel
from models.country import Country
from models.city import City
from models.sport import Sport
from models.team import Team
from models.game_invite import GameInvite
from models.user import User
from models.team_invite import TeamInvite
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv

classes = {
    "Country": Country,
    "City": City,
    "Sport": Sport,
    "Team": Team,
    "GameInvite": GameInvite,
    "User": User,
    "TeamInvite": TeamInvite
}

class Storage:
    """
    The Database Storage class, responsible for managing the application's data.

    Attributes:
        __engine: An SQLAlchemy engine instance that connects to the database.
        __session: An SQLAlchemy session instance that provides an interface to the database.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the storage object"""
        # Get environment variables
        TZ_MYSQL_USER = getenv('TZ_MYSQL_USER')
        TZ_MYSQL_PWD = getenv('TZ_MYSQL_PWD')
        TZ_MYSQL_HOST = getenv('TZ_MYSQL_HOST')
        TZ_MYSQL_DB = getenv('TZ_MYSQL_DB')
        TZ_ENV = getenv('TZ_ENV')

        # Create SQLAlchemy engine instance
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(TZ_MYSQL_USER,
                                             TZ_MYSQL_PWD,
                                             TZ_MYSQL_HOST,
                                             TZ_MYSQL_DB))
        # Drop all tables in the database if in test environment
        if TZ_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries the current database session.

        Args:
            cls: A class object. If given, only instances of that class are returned.

        Returns:
            A dictionary of instances, with their keys in the format <classname>.<instance id>.
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """
        Adds the given object to the database.

        Args:
            obj: An instance of a model class.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes to the database.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes the given object from the database.

        Args:
            obj: An instance of a model class. If not given, nothing happens.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads the database session by creating a new SQLAlchemy session instance.
        """
        # Create all tables if they don't exist
        Base.metadata.create_all(self.__engine)

        # Create a new SQLAlchemy session instance
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """
        Closes the current database session.
        """
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object with the given ID of the given class.
        If the class is not valid, it returns None.
        """
        if cls not in classes.values():
            return None
        
        obj = self.__session.query(cls).filter(cls.id == id).first()
        return obj

    def count(self, cls=None):
        """
        Returns the number of objects of a given class.
        If no class is provided, it returns the total number of objects.
        """
        from models import storage
        
        clses = classes.values()
        if not cls:
            count = 0
            for clas in clses:
                count += len(storage.all(clas).values())
        else:
            count = len(storage.all(cls).values())

        return count
    
    def query(self, cls, attribute, value, all=False):
        """
        Query object based on attribute

        Args:
            cls: Object's class
            attribute: Object's attribute to filter by
            value: Value of `attribute`
            all: Boolen to filer all or one object, default is False
        
        Return: all=False --> Object if exists
                all=True  --> List of objects if exists
                Or None
        """
        if cls not in classes.values():
            return None
        
        try:
            if all:
                return self.__session.query(cls).filter(getattr(cls, attribute) == value).all()
            else:
                return self.__session.query(cls).filter(getattr(cls, attribute) == value).first()
        except AttributeError:
            return None
