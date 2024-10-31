import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    # TestCase for rectangle.py

    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        res = rectangle.area(-1, 342)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_perimeter_count(self):
        res = rectangle.perimeter(2, 3)
        self.assertEqual(res, 10)

    def test_zero_side_perimeter(self):
        res = rectangle.perimeter(0, 2)
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        res = rectangle.perimeter(-10, -2)
        self.assertEqual(res, 0)
