#!/usr/bin/python3
"""
Test the sport class
"""

from datetime import datetime
import models
import unittest

BaseModel = models.base_model.BaseModel
Sport = models.sport.Sport

class TestSport(unittest.TestCase):
    """Test the sport class"""
    def test_is_subclass(self):
        """Test that sport is a subclass of BaseModel"""
        sport = Sport()
        self.assertIsInstance(sport, BaseModel)
        self.assertTrue(hasattr(sport, "id"))
        self.assertTrue(hasattr(sport, "created_at"))
        self.assertTrue(hasattr(sport, "updated_at"))

    def test_name_attr(self):
        """Test that sport has attribute name and is an empty string"""
        sport = Sport()
        self.assertTrue(hasattr(sport, "name"))
        self.assertEqual(sport.name, None)

    def test_todict_creates_dict(self):
        """Test to_dict method """
        sport = Sport()
        new_dict = sport.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Test that values in dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        sport = Sport()
        new_dict = sport.to_dict()
        self.assertEqual(new_dict["__class__"], "Sport")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], sport.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"], sport.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        sport = Sport()
        string = "[Sport] ({}) {}".format(sport.id, sport.__dict__)
        self.assertEqual(string, str(sport))
