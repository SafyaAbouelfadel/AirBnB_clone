#!/usr/bin/python3
"""Define the FileStorage class."""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """Manage the storage of objects in a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): A dictionary containing
            objects stored with their keys.

    Methods:
        all: Return the dictionary of stored objects (__objects).
        new: Set an object in __objects with the key `<obj class name>.id`.
        save: Serialize __objects to the JSON file.
        reload: Deserialize the JSON file to __objects, if it exists.
    """
    __file_path = file.json
    __objects = {}

    def all(self) -> dict:
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj) -> None:
        """Set in __objects the obj with key `<obj class name>.id`."""
        FileStorage.__objects[obj.__class.__name + "." + obj.id]

    def save(self) -> None:
        """serializes __objects to the JSON file"""
        temp_dict = dict()
        for keys in self.__objects.keys():
            temp_dict[keys] = self.__objects[keys].to_dict()
        with open(self.__file_path, mode='w') as jsonfile:
            json.dump(temp_dict, jsonfile)
            
    def reload(self) -> None:
        """deserializes the JSON file to __objects"""
        try:
            # to-do reload
            
        except:
            pass
