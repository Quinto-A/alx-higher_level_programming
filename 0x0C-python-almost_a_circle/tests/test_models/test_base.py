#!/usr/bin/python3


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_provided(self):
        bi = Base(10)
        self.assertEqual(bi.id, 10)

if __name__ == '__main__':
    unittest.main()
