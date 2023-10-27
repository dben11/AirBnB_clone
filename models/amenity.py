#!/usr/bin/python3
"""Holds class Amenity"""

import models
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Representation of Amenity"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize amenity"""
        super().__init__(*args, **kwargs)
