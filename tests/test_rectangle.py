import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_10_5(self):
        self.assertEqual(area(10, 5), 50)

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_square_case(self):
        self.assertEqual(area(10, 10), 100)

    def test_perimeter_10_5(self):
        self.assertEqual(perimeter(10, 5), 30)

    def test_perimeter_3_4(self):
        self.assertEqual(perimeter(3, 4), 14)


if __name__ == '__main__':
    unittest.main()
