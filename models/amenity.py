#!/usr/bin/python3
"""Module for Amenity class."""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Class representing a Amenity."""
    name = ""
    
    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
