#!/usr/bin/python3
"""
Test the team class
"""

from datetime import datetime
import models
import unittest

BaseModel = models.base_model.BaseModel
Team = models.team.Team

class Testteam(unittest.TestCase):
    """Test the team class"""
    def test_is_subclass(self):
        """Test that team is a subclass of BaseModel"""
        team = Team()
        self.assertIsInstance(team, BaseModel)
        self.assertTrue(hasattr(team, "id"))
        self.assertTrue(hasattr(team, "created_at"))
        self.assertTrue(hasattr(team, "updated_at"))

    def test_name_attr(self):
        """Test that team has attribute name and empty string"""
        team = Team()
        self.assertTrue(hasattr(team, "name"))
        self.assertEqual(team.name, None)

    def test_bio_attr(self):
        """Test that team has attribute bio and empty string"""
        team = Team()
        self.assertTrue(hasattr(team, "bio"))
        self.assertEqual(team.bio, None)

    def test_image_attr(self):
        """Test that team has attribute image and empty string"""
        team = Team()
        self.assertTrue(hasattr(team, "image"))
        self.assertEqual(team.image, None)

    def test_sport_id_attr(self):
        """Test that team has attribute sport id and None"""
        team = Team()
        self.assertTrue(hasattr(team, "sport_id"))
        self.assertEqual(team.sport_id, None)

    def test_city_id_attr(self):
        """Test that team has attribute city id and None"""
        team = Team()
        self.assertTrue(hasattr(team, "city_id"))
        self.assertEqual(team.city_id, None)

    def test_leader_id_attr(self):
        """Test that team has attribute leader id and None"""
        team = Team()
        self.assertTrue(hasattr(team, "leader_id"))
        self.assertEqual(team.leader_id, None)

    def test_todict_creates_dict(self):
        """Test to_dict method """
        team = Team()
        new_dict = team.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Test that values in dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        team = Team()
        new_dict = team.to_dict()
        self.assertEqual(new_dict["__class__"], "Team")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], team.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"], team.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        team = Team()
        string = "[Team] ({}) {}".format(team.id, team.__dict__)
        self.assertEqual(string, str(team))
