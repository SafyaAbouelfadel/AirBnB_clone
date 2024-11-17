#!/usr/bin/python3
"""file containing basemodel class"""
from datetime import datetime
import models
from uuid import uuid4


class BaseModel(object):
    """Represents the BaseModel of the HBnB project.

    Attributes:
        id (str): A unique identifier generated using the uuid4() function.
        created_at (datetime): The date & time
            when the instance is created.
        updated_at (datetime): The date & time
            when the instance is last updated.

    Methods:
        __init__: Initializes a new instance of the BaseModel class.
        __str__: Returns a string representation of the BaseModel instance.
        save: Updates the 'updated_at' attribute and saves the instance.
        to_dict: Returns a dictionary representation of the BaseModel instance.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class.

        Args:
            *args: Not Used.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """class str method"""
        return "[{}]({}){}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        ''' updates updated_at with the current time'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''  returns a dictionary of the instance'''
        self_dict = self.__dict__.copy()
        self_dict['__class__'] = self.__class__.__name__
        self_dict['created_at'] = self.created_at.isoformat()
        self_dict['created_at'] = self.updated_at.isoformat()
        return self_dict
