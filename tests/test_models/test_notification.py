"""
Test the notification class
"""

from datetime import datetime
import models
import unittest

BaseModel = models.base_model.BaseModel
Notification = models.notification.Notification

class TestNotification(unittest.TestCase):
    """Test the notification class"""
    def test_is_subclass(self):
        """Test that notification is a subclass of BaseModel"""
        notification = Notification()
        self.assertIsInstance(notification, BaseModel)
        self.assertTrue(hasattr(notification, "id"))
        self.assertTrue(hasattr(notification, "created_at"))
        self.assertTrue(hasattr(notification, "updated_at"))

    def test_status_attr(self):
        """Test that notification has attribute status and is an False"""
        notification = Notification()
        self.assertTrue(hasattr(notification, "status"))
        self.assertEqual(notification.status, None)

    def test_message_attr(self):
        """Test that notification has attribute message and is an empty string"""
        notification = Notification()
        self.assertTrue(hasattr(notification, "message"))
        self.assertEqual(notification.message, None)

    def test_sender_id_attr(self):
        """Test that notification has attribute sender id and None"""
        notification = Notification()
        self.assertTrue(hasattr(notification, "sender_id"))
        self.assertEqual(notification.sender_id, None)

    def test_receiver_id_attr(self):
        """Test that notification has attribute receiver id and None"""
        notification = Notification()
        self.assertTrue(hasattr(notification, "receiver_id"))
        self.assertEqual(notification.receiver_id, None)

    def test_todict_creates_dict(self):
        """Test to_dict method """
        notification = Notification()
        new_dict = notification.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Test that values in dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        notification = Notification()
        new_dict = notification.to_dict()
        self.assertEqual(new_dict["__class__"], "Notification")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], notification.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"], notification.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        notification = Notification()
        string = "[Notification] ({}) {}".format(notification.id, notification.__dict__)
        self.assertEqual(string, str(notification))
