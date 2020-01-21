#!/usr/bin/python3
"""This is the databasestorage class for AirBnB"""
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class store in databases the objects"""
    __session = None
    __engine = None

    def __init__(self):
        """all begins here"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        a = dict()
        clasesitas = ["State", "City", "User", "Place", "Review", "Amenity"]
        # if cls != None:
        # objre = self.__session.query(cls.__name__).all()
        # print("Esto esta botando el all del datastorage", objre)
        # for obj in objre:
        # print("en teoria esto es cada objeto", obj.__dict__)
        # print("el id en teoria obj.id", obj.id)
        # a[obj.id] = obj.to_dict()
        # else:
        for clase in clasesitas:
            objre = self.__session.query(eval(clase)).all()
            for obj in objre:
                # print("cada objeto cuando no hay clase", obj.to_dict())
                # print("este es el objeto", obj)
                a[type(obj).__name__+"."+obj.id] = obj
                # key = "{}.{}".format(type(obj).__name__, obj.id)
        return a

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commiting changes
        """
        self.__session.commit()

    def reload(self):
        """Create metadata for all
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()

    def delete(self, obj=None):
        """Delete object"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """ close session calling method remove or close """
        self.__session.close()
