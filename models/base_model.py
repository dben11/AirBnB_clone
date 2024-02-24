#!/usr/bin/python3
"""
A class BaseModel that defines all
common attributes/methods for other
classes
"""
import models
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A parent class

    Attributes:
        id: a unique id of an instance of the class
        created_at: current datetime when an instance is created
        updated_at: created_at updated

    Methods:
        __str__: magic that print string representation
        save: updates the public instance attr updated_at
              with the current datetime
        to_dict: return a dictionary containing
                 all keys/values of __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """Constructor"""

        if kwargs is not None:
            for attr, value in kwargs.items():
                if attr != '__class__':
                    if attr == 'created_at' or attr == 'updated_at':
                        self.__dict__[attr] = datetime.strptime(value, time)
                    else:
                        self.__dict__[attr] = value

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """Print string representation"""
        return "[{}] ({}) {}".format(__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """save the updated datetime"""
        self.__dict__['updated_at'] = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dup_dict = self.__dict__.copy()

        dup_dict['__class__'] = __class__.__name__
        dup_dict['created_at'] = self.created_at.isoformat()
        dup_dict['updated_at'] = self.updated_at.isoformat()
        return dup_dict
