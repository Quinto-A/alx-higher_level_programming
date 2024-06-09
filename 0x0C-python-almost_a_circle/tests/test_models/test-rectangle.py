#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Rectangle._Base__nb_objects = 0

    def test_Rectangle_creation_with_id(self):
        r1 = Rectangle(10, 20, 2, 3, 100)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)

    def test_Rectangle_creation_without_id(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_Rectangle_auto_increment_id(self):
        r1 = Rectangle(10, 20)
        r2 = Rectangle(30, 40)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_Rectangle_setter_getters(self):
        r1 = Rectangle(10, 20)
        r1.width = 15
        r1.height = 25
        r1.x = 5
        r1.y = 10
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 25)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 10)

    def test_initialization_invalid_width_type(self):
        with self.assertRaises(TypeError) as e:
            Rectangle("10", 20)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_initialization_invalid_width_value(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(-10, 20)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_initialization_invalid_height_type(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "20")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_initialization_invalid_height_value(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, -20)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_initialization_invalid_x_type(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 20, "1", 2)
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_initialization_invalid_x_value(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 20, -1, 2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_initialization_invalid_y_type(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 20, 1, "2")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_initialization_invalid_y_value(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 20, 1, -2)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_setter_valid_width(self):
        r = Rectangle(10, 20)
        r.width = 30
        self.assertEqual(r.width, 30)

    def test_setter_invalid_width(self):
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError) as e:
            r.width = "30"
        self.assertEqual(str(e.exception), "width must be an integer")

if __name__ == '__main__':
    unittest.main()
