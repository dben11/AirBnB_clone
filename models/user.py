#!/usr/bin/python3
"""Holds class User"""

import models
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """Representation of place"""
    email = ""
    password = ""
    first_name = ""
    last_naame = ""

    def __init__(self, *args, **kwargs):
        """Initialize user"""
        super().__init__(*args, **kwargs)
