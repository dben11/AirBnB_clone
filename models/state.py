#!/usr/bin/python3
"""Holds class State"""


from models.base_model import BaseModel
import models


class State(BaseModel):
    """Representation of state """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
