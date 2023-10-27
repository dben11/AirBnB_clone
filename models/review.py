#!/usr/bin/python3
"""Holds class Review"""

import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of review"""
    place_id = ""
    uuser_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize city"""
        super().__init__(*args, **kwargs)
