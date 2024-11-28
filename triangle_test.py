import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    # TestCase for triangle.py

    def test_triangle_zero_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_triangle_area(self):
        res = triangle.area(5, 2)
        self.assertEqual(res, 5)

    def test_negative_area(self):
        res = triangle.area(-1, -100)
        self.assertEqual(res, 0)

    def test_triangle_zero_perimeter(self):
        res = triangle.perimeter(0, 1, 0)
        self.assertEqual(res, 0)

    def test_triangle_perimeter(self):
        res = triangle.perimeter(2, 1, 5)
        self.assertEqual(res, 8)

    def test_negative_perimeter(self):
        res = triangle.perimeter(-1, -2, -3)
        self.assertEqual(res, 0)
