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
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj) -> None:
        """Set in __objects the obj with key `<obj class name>.id`."""
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__,
            obj.id
        )] = obj

    def save(self) -> None:
        """serializes __objects to the JSON file"""
        temp_dict = {}
        for keys in self.__objects:
            temp_dict[keys] = self.__objects[keys].to_dict()
        with open(self.__file_path, "w") as fj:
            json.dump(temp_dict, fj)

    def reload(self) -> None:
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as fl:
                dct_objt = json.load(fl)
                for objt in dct_objt.values():
                    clss_name = objt["__class__"]
                    del objt["__class__"]
                    self.new(eval(clss_name)(**objt))
        except:
            pass
