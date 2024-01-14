#!/usr/bin/python3
<<<<<<< HEAD
"""cREATING subclass FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    serialize JSON File to objects and deserialization
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def classes(self):
        """Returns a list of available classes"""

        return list(set(obj.__class__.__name__ for obj in self.__objects.values()))

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'User':
                        class_obj = User
                    else:
                        class_obj = globals()[class_name]
                    obj_instance = class_obj(**obj_dict)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass

import json
from models.base_model import BaseModel


class FileStorage:
    """A class for handling storage to/from a JSON file."""
    def __init__(self, file_path):
        """class constructor"""
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """Retrieve all objects in the storage"""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Save objects to the JSON file"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
            with open(self.__file_path, 'w') as file:
                json.dump(serialized_objects, file)

    def reload(self):
        """Reload objects from the JSON file"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_instance = globals().get(class_name)
                    if class_instance:
                        instance = class_instance(**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass
