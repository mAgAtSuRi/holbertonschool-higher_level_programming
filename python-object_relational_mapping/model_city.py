#!/usr/bin/python3
"""
This module contains a schema for database hbtn_0e_6_usa
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    This class is a schema
    of the city table
    """

    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State")
