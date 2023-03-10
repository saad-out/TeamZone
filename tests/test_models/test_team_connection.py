#!/usr/bin/python3
"""
Test the teamconnection class
"""

from datetime import datetime
import models
import unittest

BaseModel = models.base_model.BaseModel
TeamConnection = models.team_connection.TeamConnection

class TestTeamConnection(unittest.TestCase):
    """Test the teamconnection class"""
    def test_is_subclass(self):
        """Test that teamconnection is a subclass of BaseModel"""
        teamconnection = TeamConnection()
        self.assertIsInstance(teamconnection, BaseModel)
        self.assertTrue(hasattr(teamconnection, "id"))
        self.assertTrue(hasattr(teamconnection, "created_at"))
        self.assertTrue(hasattr(teamconnection, "updated_at"))

    def test_game_date_attr(self):
        """Test that teamconnection has attribute game_date"""
        teamconnection = TeamConnection()
        self.assertTrue(hasattr(teamconnection, "game_date"))
        #self.assertEqual(type(teamconnection.game_date), None)
        
    def test_is_completed_attr(self):
        """Test that teamconnection has attribute is_completed"""
        teamconnection = TeamConnection()
        self.assertTrue(hasattr(teamconnection, "is_completed"))
        self.assertEqual(teamconnection.is_completed, None)

    def test_team_one_score_attr(self):
        """Test that teamconnection has attribute team_one_score"""
        teamconnection = TeamConnection()
        self.assertTrue(hasattr(teamconnection, "team_one_score"))
        #self.assertEqual(type(teamconnection.team_one_score), int)

    def test_team_two_score_attr(self):
        """Test that teamconnection has attribute team_two_score"""
        teamconnection = TeamConnection()
        self.assertTrue(hasattr(teamconnection, "team_two_score"))
        #self.assertEqual(type(teamconnection.team_two_score), int)

    def test_todict_creates_dict(self):
        """Test to_dict method """
        teamconnection = TeamConnection()
        new_dict = teamconnection.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Test that values in dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        teamconnection = TeamConnection()
        new_dict = teamconnection.to_dict()
        self.assertEqual(new_dict["__class__"], "TeamConnection")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], teamconnection.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"], teamconnection.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        teamconnection = TeamConnection()
        string = "[TeamConnection] ({}) {}".format(teamconnection.id, teamconnection.__dict__)
        self.assertEqual(string, str(teamconnection))
