import math
import unittest
from triangle import area, perimeter


def heron_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


class TriangleTestCase(unittest.TestCase):
    def test_area_3_4_5(self):
        self.assertAlmostEqual(area(3, 4, 5), heron_area(3, 4, 5))

    def test_area_5_5_6(self):
        self.assertAlmostEqual(area(5, 5, 6), heron_area(5, 5, 6))

    def test_perimeter_3_4_5(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_2_3_4(self):
        self.assertEqual(perimeter(2, 3, 4), 9)


if __name__ == '__main__':
    unittest.main()
