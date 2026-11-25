import math
import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_radius_5(self):
        self.assertAlmostEqual(area(5), math.pi * 25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_radius_5(self):
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)


if __name__ == '__main__':
    unittest.main()
