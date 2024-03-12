#!/usr/bin/python3
"""Defines unittests for BaseModel class"""

import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_no_args_instantiates(self):
        """Test no arguments"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        """Test id"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """Test created at"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test updated at"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_different_created_at(self):
        """Test two models"""
        base_model_instance1 = BaseModel()
        base_model_instance2 = BaseModel()
        self.assertNotEqual(base_model_instance1.id, base_model_instance2.id)

    def test_two_models_different_created_at(self):
        """Test two modes"""
        b_m_instance1 = BaseModel()
        sleep(0.05)
        b_m_instance2 = BaseModel()
        self.assertLess(b_m_instance1.created_at, b_m_instance2.created_at)

    def test_two_models_different_created_at(self):
        """Test two modes"""
        b_m_instance1 = BaseModel()
        sleep(0.05)
        b_m_instance2 = BaseModel()
        self.assertLess(b_m_instance1.updated_at, b_m_instance2.updated_at)

    def test_init(self):
        """Test initialization of BaseModel instance"""
        base_model_instance = BaseModel()
        self.assertIsInstance(base_model_instance, BaseModel)
        self.assertTrue(hasattr(base_model_instance, 'id'))
        self.assertTrue(hasattr(base_model_instance, 'created_at'))
        self.assertTrue(hasattr(base_model_instance, 'updated_at'))
        self.assertIsInstance(base_model_instance.created_at, datetime)
        self.assertIsInstance(base_model_instance.updated_at, datetime)

    def test_instantiation_with_kwargs(self):
        """Test kwargs"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        base_model_instance = BaseModel()
        base_model_dict = base_model_instance.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(datetime.fromisoformat(
                    base_model_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(
                    base_model_dict['updated_at']), datetime)

    def test_str(self):
        """Test the __str__ method of BaseModel"""
        base_model_instance = BaseModel()
        base_model_str = str(base_model_instance)
        self.assertIn('BaseModel', base_model_str)
        self.assertIn(base_model_instance.id, base_model_str)


if __name__ == "__main__":
    unittest.main()
