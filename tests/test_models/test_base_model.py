#!/usr/bin/python3
"""Building BaseModel unit test"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel_instantiation(unittest.TestCase):
    """Testing instantiation"""

    def test_instantiation(self):
        """Testing Instantiation"""
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)

        my_model.name = "My First Model"
        my_model.my_number = 89

        attr_dict = {
                "id": str,
                "created_at": datetime,
                "updated_at": datetime,
                "name": str,
                "my_number": int
                }
        for attr, typ in attr_dict.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, my_model.__dict__)
                self.assertIs(type(my_model.__dict__[attr]), typ)


class TestBaseModel_save(unittest.TestCase):
    """Testing for the save method of the instance class"""

    def test_save(self):
        """Testing if save method is successfully executed"""
        my_model = BaseModel()
        first_updated_at = my_model.updated_at
        sleep(0.05)
        my_model.save()
        second_updated_at = my_model.updated_at
        self.assertLess(first_updated_at, second_updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Testing the to_dict method"""

    def test_to_dict(self):
        """Testing if the to_dict method successfully return a dict"""
        my_model = BaseModel()
        self.assertTrue(type(my_model.to_dict), dict)


if __name__ == '__main__':
    unittest.main()
