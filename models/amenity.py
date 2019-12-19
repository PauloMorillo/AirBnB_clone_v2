#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",
                                       secondary=place_amenity,
                                       back_populates="amenities")

    else:
        name = ""
