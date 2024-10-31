import unittest
import math
import circle

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_circle_area(self):
        res = circle.area(3)
        self.assertEqual(res, 3 * 3 * math.pi)

    def test_circle_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 5 * 2 * math.pi)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
