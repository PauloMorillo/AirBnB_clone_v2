#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship
from models.city import City
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ""

    @property
    def cities(self):
        """getter cities"""
        a = []
        for value in models.storage.all(City).values():
            if value.state_id == self.id:
                a.append(value)
        return a
