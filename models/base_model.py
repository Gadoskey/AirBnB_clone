#!/usr/bin/python3

"""Defines class BaseModel"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel instance

        Args:
            *args: unused
            **kwargs: key / value pairs
        """
        t_f = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            if kwargs != "__class__":
                for key, value in kwargs.items():
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, t_f))
                    else:
                        setattr(self, key, value)

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """string representation of all class instance and its attributes"""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
