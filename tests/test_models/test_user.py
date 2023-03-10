#!/usr/bin/python3
"""
Test the user class
"""

from datetime import datetime
import models
import unittest

BaseModel = models.base_model.BaseModel
User = models.user.User

class TestUser(unittest.TestCase):
    """Test the user class"""
    def test_is_subclass(self):
        """Test that user is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_name_attr(self):
        """Test that user has attribute name and is an empty"""
        user = User()
        self.assertTrue(hasattr(user, "name"))
        self.assertEqual(user.name, None)

    def test_image_attr(self):
        """Test that user has attribute image and empty string"""
        user = User()
        self.assertTrue(hasattr(user, "image"))
        self.assertEqual(user.image, None)

    def test_username_attr(self):
        """Test that user has attribute username and is an empty"""
        user = User()
        self.assertTrue(hasattr(user, "username"))
        self.assertEqual(user.username, None)

    def test_email_attr(self):
        """Test that user has attribute email and is an empty"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, None)

    def test_password_attr(self):
        """Test that user has attribute password and is an empty"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, None)

    def test_todict_creates_dict(self):
        """Test to_dict method """
        user = User()
        new_dict = user.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Test that values in dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        user = User()
        new_dict = user.to_dict()
        self.assertEqual(new_dict["__class__"], "User")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], user.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"], user.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))
