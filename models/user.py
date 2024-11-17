#!/usr/bin/python3
"""Represents the User Class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that represents a user instant

    Attributes:
        email (str): email address of the user.
        password (str): password associated with the user.
        first_name (str): first name of the user.
        last_name (str): last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
