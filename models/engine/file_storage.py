#!/usr/bin/python3
"""file storage module"""

import json
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """Serializes instances to a JSON file
    & deserializes back to instnaces"""

    # string - path to the json file
    __file_path = "file.json"
    # Dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Set the key-value pair in __objects
        (class.id as key, obj as the value)"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {}
        for key in self.__objects:
            if key == "password":
                json_obj[key].decode()
            json_obj[key] = self.__objects[key].to_dict(save_fs=1)
        with open(self.__file_path, 'w') as obj_file:
            json.dump(json_obj, obj_file, default=str)

    def reload(self):
        """Deserializes the JSON file to_objects"""
        try:
            with open(self.__file_path, 'r') as obj_file:
                js = json.load(obj_file)
            for key in js:
                self.__objects[key] = classes[js[key]["__class__"]](**js[key])
        except Exception:
            pass

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """Return the object based on the class name and its ID,
        None if not found
        """
        if cls not in classes.values():
            return None
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
        return None

    def count(self, cls=None):
        """Count the number of objects in storage"""
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())
        return count
