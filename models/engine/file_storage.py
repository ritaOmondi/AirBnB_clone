#!/usr/bin/python3
"""cREATING subclass FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User

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

