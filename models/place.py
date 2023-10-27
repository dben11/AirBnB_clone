#!/usr/bin/python3
"""Holds class Place"""

import models
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """Representation of place"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize place"""
        super().__init__(*args, **kwargs)
