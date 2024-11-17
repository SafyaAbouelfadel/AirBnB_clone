#!/usr/bin/python3
"""represents a Review Class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class that represents a review instant

    Attributes:
        place_id (str): ID of the place associated with the review.
        user_id (str): ID of the user who wrote the review.
        text (str): content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
