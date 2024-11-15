#!/usr/bin/python3
"""file containing basemodel class"""
from datetime import datetime
from models import storage
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

    def __init__(self, *arg, **kwargs):
        """Initialize a new instance of the BaseModel class.

        Args:
            *args: Not Used.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    # Check if value is already a datetime object
                    if isinstance(value, datetime):
                        setattr(self, key, value)
                    else:
                        tm = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, tm)
                elif key != "__class__":
                    setattr(self, key, value)

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
        storage.save()

    def to_dict(self):
        '''  returns a dictionary of the instance'''
        self_dict = dict(self.__dict__)
        self_dict['__class__'] = self.__class__.__name__
        self_dict['created_at'] = datetime.isoformat(self.created_at)
        self_dict['created_at'] = datetime.isoformat(self.created_at)
        return self_dict
