#!/usr/bin/python3
"""This module define the BaseModel class"""


import uuid
from datetime import datetime
import models
from os import getenv

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A class that defines all common attr/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Instantiation of a class attribute"""

        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    setattr(self, key, val)

            if kwargs.get("created_at", None)\
                    and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()

            if kwargs.get("updated_at", None)\
                    and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.update_at = self.created_at

    def __str__(self):
        """String representation of the output in dict format"""

        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Updates the public instance attr updated_at"""

        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_fs=None):
        """Returns a dict containing key/value of __dict__ of the instance"""

        dict_format = self.__dict__.copy()
        if "created_at" in dict_format:
            dict_format["created_at"] =\
                    dict_format["created_at"].strftime(time)

        if "updated_at" in dict_format:
            dict_format["updated_at"] =\
                    dict_format["updated_at"].strftime(time)

        dict_format["__class__"] = self.__class__.__name__

        if "_sa_instance_state" in dict_format:
            del dict_format["_sa_instance_state"]

        if save_fs is None:
            if "password" in dict_format:
                del dict_format["password"]

        return dict_format

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
