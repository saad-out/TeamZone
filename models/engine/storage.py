import models
from models.base_model import Base, BaseModel
from models.country import Country
from models.city import City
from models.sport import Sport
from models.team import Team
from models.team_connection import TeamConnection
from models.user import User
from models.notification import Notification
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv

classes = {
    "Country": Country,
    "City": City,
    "Sport": Sport,
    "Team": Team,
    "TeamConnection": TeamConnection,
    "User": User,
    "Notification": Notification
}

class Storage:
    """The Database Storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the storage object"""
        TZ_MYSQL_USER = getenv('TZ_MYSQL_USER')
        TZ_MYSQL_PWD = getenv('TZ_MYSQL_PWD')
        TZ_MYSQL_HOST = getenv('TZ_MYSQL_HOST')
        TZ_MYSQL_DB = getenv('TZ_MYSQL_DB')
        TZ_ENV = getenv('TZ_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(TZ_MYSQL_USER,
                                             TZ_MYSQL_PWD,
                                             TZ_MYSQL_HOST,
                                             TZ_MYSQL_DB))
        if TZ_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """Add the object to the database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove method on the session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """Return the object based on the class and it id"""
        if cls not in classes.values():
            return None
        
        obj = self.__session.query(cls).filter(cls.id == id).first()
        return obj

    def count(self, cls=None):
        """count the number of objects"""
        clses = classes.values()
        if not cls:
            count = 0
            for clas in clses:
                count += len(model.storage.all(clas).values())
        else:
            count = len(model.storage.all(cls).values())

        return count
