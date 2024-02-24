#!/usr/bin/python3
"""Defining FileStorage class to handle strorage"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class

    Attribute:
        __file_path (str): path to the JSON file save to
        __objects (dict): empty but will store all objects by classnameid
    """

    # Private class attributes

    __file_path = "file.json"
    __objects = {}

    # Public Instance methods

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in dictionary the obj with key <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON file (path: __file_path)"""

        all_objs = FileStorage.__objects
        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as filename:
            json.dump(obj_dict, filename)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as fname:
                try:
                    obj_dict = json.load(fname)

                    for key, value in obj_dict.items():
                        cls_name, obj_id = key.split('.')

                        cls = eval(cls_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
