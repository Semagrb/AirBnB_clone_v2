#!/usr/bin/python3
"""This is the city class"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place

class City(BaseModel, Base):
    """City class for storing city information."""
    __tablename__ = "cities"

    # Columns definition
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # Relationship with the Place class
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="city")
