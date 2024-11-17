#!/usr/bin/python3
"""Module that defines City Class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that represents a city.

    Attributes:
        state_id (str): The ID of the state of the city.
        name (str): name of the city.
    """

    state_id = ""
    name = ""
