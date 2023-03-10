#!/usr/bin/python3
"""
Test the city class
"""

from datetime import datetime
import models
import unittest

BaseModel = models.base_model.BaseModel
City = models.city.City

class TestCity(unittest.TestCase):
    """Test the city class"""
    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name_attr(self):
        """Test that city has attribute name and is an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, None)

    def test_country_id_attr(self):
        """Test that city has attribute country id and is an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "country_id"))
        self.assertEqual(city.country_id, None)

    def test_todict_creates_dict(self):
        """Test to_dict method """
        city = City()
        new_dict = city.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Test that values in dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        city = City()
        new_dict = city.to_dict()
        self.assertEqual(new_dict["__class__"], "City")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], city.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"], city.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
