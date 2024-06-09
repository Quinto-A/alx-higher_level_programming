#!/usr/bin/python3


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_provided(self):
        bi = Base(10)
        self.assertEqual(bi.id, 10)

    def test_mixed_ids(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(100)
        self.assertEqual(b2.id, 100)
        b3 = Base()
        self.assertEqual(b3.id, 2)

if __name__ == '__main__':
    unittest.main()
