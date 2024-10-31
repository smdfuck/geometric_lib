import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    def test_triangle_zero_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_triangle_area(self):
        res = triangle.area(5, 2)
        self.assertEqual(res, 5)

    def test_triangle_zero_perimeter(self):
        res = triangle.perimeter(0, 1, 0)
        self.assertEqual(res, 0)

    def test_triangle_perimeter(self):
        res = triangle.perimeter(2, 1, 5)
        self.assertEqual(res, 8)
