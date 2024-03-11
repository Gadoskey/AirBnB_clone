#!/usr/bin/python3
"""Defines unittests for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test environment"""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down test environment"""
        del self.model

    def test_id_generation(self):
        """Test if a unique id is generated for each BaseModel instance"""
        other_model = BaseModel()
        self.assertNotEqual(self.model.id, other_model.id)

    def test_created_updated_at(self):
        """Test if created_at and updated_at attributes are set correctly"""
        time_difference = self.model.updated_at - self.model.created_at
        self.assertLessEqual(time_difference.total_seconds(), 1)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel"""
        model_dict = self.model.to_dict()
        """Check if the returned dictionary contains all expected keys"""
        self.assertIn('id', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        """Check if the __class__ key has the correct value"""
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        """Check if created_at and updated_at are in ISO format strings"""
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
