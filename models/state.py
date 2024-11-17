#!/usr/bin/python3
"""Module that dfines a State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class that represent a state instance

    Attributes:
        name (str): name of the geographical state.
    """
    name = ""
