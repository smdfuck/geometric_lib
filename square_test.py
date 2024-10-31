import unittest
import square

class SquareTestCase(unittest.TestCase):
    # TestCase for square.py
 
    def test_square_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = square.area(2)
        self.assertEqual(res, 4)

    def test_square_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimeter(self):
        res = square.perimeter(2)
        self.assertEqual(res, 8)
