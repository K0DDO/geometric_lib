import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_side_4(self):
        self.assertEqual(area(4), 16)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_side_4(self):
        self.assertEqual(perimeter(4), 16)

    def test_perimeter_side_10(self):
        self.assertEqual(perimeter(10), 40)


if __name__ == '__main__':
    unittest.main()
