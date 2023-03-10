#!/usr/bin/python3
"""
Test the country class
"""

from datetime import datetime
import models
import unittest

BaseModel = models.base_model.BaseModel
Country = models.country.Country

class TestCountry(unittest.TestCase):
    """Test the country class"""
    def test_is_subclass(self):
        """Test that country is a subclass of BaseModel"""
        country = Country()
        self.assertIsInstance(country, BaseModel)
        self.assertTrue(hasattr(country, "id"))
        self.assertTrue(hasattr(country, "created_at"))
        self.assertTrue(hasattr(country, "updated_at"))

    def test_name_attr(self):
        """Test that country has attribute name and is an empty string"""
        country = Country()
        self.assertTrue(hasattr(country, "name"))
        self.assertEqual(country.name, None)

    def test_todict_creates_dict(self):
        """Test to_dict method """
        country = Country()
        new_dict = country.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Test that values in dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        country = Country()
        new_dict = country.to_dict()
        self.assertEqual(new_dict["__class__"], "Country")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], country.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"], country.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        country = Country()
        string = "[Country] ({}) {}".format(country.id, country.__dict__)
        self.assertEqual(string, str(country))
