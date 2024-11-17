#!/usr/bin/python3
"""Module that represent class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class tha represents a Place instances

    Attributes:
        city_id (str): ID of the city to which the place belongs.
        user_id (str): ID of the user associated with the place.
        name (str): name of the place.
        description (str): details about the place.
        number_rooms (int): number of rooms in the place.
        number_bathrooms (int): number of bathrooms in the place.
        max_guest (int): maximum number of guests
            the place can accommodate.
        price_by_night (int): price per night for the place.
        latitude (float): latitude coordinate of the place.
        longitude (float): longitude coordinate of the place.
        amenity_ids (list): List of The ID of the amenity associated
            with the place.
    """

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
