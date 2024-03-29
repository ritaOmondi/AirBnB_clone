#!/usr/bin/python3
"""
Perform test for TestBaseModel
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """test class to tests methods"""
    def test_init_with_kwargs(self):
        """test kwargs"""
        data = {'id': 'test_id', 'created_at': '2022-01-13T12:34:56.789',
                'updated_at': '2022-01-13T12:34:56.789',
                'custom_attribute': 'some_value'
                }
        instance = BaseModel(**data)
        self.assertEqual(instance.id, 'test_id')
        self.assertEqual(instance.custom_attribute, 'some_value')
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_init_without_kwargs(self):
        """test without kwargs"""
        instance = BaseModel()
        self.assertIsNotNone(instance.id)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
