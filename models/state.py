#!/usr/bin/python3
"""Holds class State"""


from models.base_model import BaseModel, Base
import models


class State(BaseModel, Base):
    """Representation of state """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
