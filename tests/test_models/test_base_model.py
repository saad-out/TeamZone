"""Test Basemodel"""
from datetime import datetime
import models
import time
import unittest
from unittest import mock

BaseModel = models.base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def test_instantiation(self):
        """Test that the obj is correctly created"""
        base = BaseModel()
        self.assertIs(type(base), BaseModel)
        base.name = "TeamZone"
        base.number = 69
        attrs_types = {
                "id": str,
                "created_at": datetime,
                "updated_at": datetime,
                "name": str,
                "number": int
                }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, base.__dict__)
                self.assertIs(type(base.__dict__[attr]), typ)
        self.assertEqual(base.name, "TeamZone")
        self.assertEqual(base.number, 69)

    def test_datetime_attributes(self):
        """Test that two BaseModel instances have different datetime"""
        tic = datetime.now()
        base1 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= base1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        base2 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= base2.created_at <= toc)
        self.assertEqual(base1.created_at, base1.updated_at)
        self.assertEqual(base2.created_at, base2.updated_at)
        self.assertNotEqual(base1.created_at, base2.created_at)
        self.assertNotEqual(base1.updated_at, base2.updated_at)


    def test_uuid(self):
        """Test that id is a valid uuid"""
        base1 = BaseModel()
        base2 = BaseModel()
        for base in [base1, base2]:
            uuid = base.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
        self.assertNotEqual(base1.id, base2.id)


    def test_to_dict(self):
        """Test the conversion of object to dictionary for JSON"""
        base = BaseModel()
        base.name = "TeamZone"
        base.number = 69
        new_dict = base.to_dict()
        attrs = ["id", "created_at", "updated_at", "name", "number", "__class__"]
        self.assertCountEqual(new_dict.keys(), attrs)
        self.assertEqual(new_dict['__class__'], 'BaseModel')
        self.assertEqual(new_dict['name'], 'TeamZone')
        self.assertEqual(new_dict['number'], 69)

    def test_to_dict_values(self):
        """test that the values in dict from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        base = BaseModel()
        new_dict = base.to_dict()
        self.assertEqual(new_dict["__class__"], "BaseModel")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], base.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"], base.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        base = BaseModel()
        string = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        self.assertEqual(string, str(base))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and call storage.save"""
        base = BaseModel()
        old_created_at = base.created_at
        old_updated_at = base.updated_at
        base.save()
        new_created_at = base.created_at
        new_updated_at = base.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)











