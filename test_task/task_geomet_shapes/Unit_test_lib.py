import unittest
import math
from shape_calculate import Circle, Triangle

class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        # Проверка правильного вычисления площади круга
        circle = Circle(5)
        expected_area = math.pi * 5 ** 2
        self.assertAlmostEqual(circle.area(), expected_area, places=5)

    def test_invalid_circle_radius(self):
        # Неверный радиус (отрицательный или ноль)
        with self.assertRaises(ValueError):
            Circle(-1)
        with self.assertRaises(ValueError):
            Circle(0)

    def test_triangle_area(self):
        # Проверка правильности вычисления площади треугольника
        triangle = Triangle(3, 4, 5)
        expected_area = 6.0
        self.assertAlmostEqual(triangle.area(), expected_area, places=5)

    def test_invalid_triangle_sides(self):
        # Невозможность сформировать треугольник (недопустимая комбинация сторон)
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)
        with self.assertRaises(ValueError):
            Triangle(0, 0, 0)

    def test_is_right_triangle(self):
        # Проверка, правильно ли определяется прямоугольный треугольник
        right_triangle = Triangle(3, 4, 5)
        non_right_triangle = Triangle(5, 5, 5)
        self.assertTrue(right_triangle.is_right_triangle())
        self.assertFalse(non_right_triangle.is_right_triangle())

if __name__ == '__main__':
    unittest.main()