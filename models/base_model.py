#!/usr/bin/python3
"""This module define the BaseModel class"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """A class that defines all common attr/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Instantiation of a class attribute"""

        if kwargs:
            del kwargs["__class__"]
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dtime = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()

    def __str__(self):
        """String representation of the output in dict format"""

        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Updates the public instance attr updated_at"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dict containing key/value of __dict__ of the instance"""

        dict_format = {}

        dict_format["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            """get the val which are of datetime object type"""

            if isinstance(val, datetime):
                dict_format[key] = val.isoformat()

            else:
                dict_format[key] = val

        return dict_format
