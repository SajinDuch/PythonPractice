'''
---✍️ ЗАДАНИЕ:
    Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь
круга по радиусу и треугольника по трем сторонам.
    Дополнительно к работоспособности:
        - Юнит-тесты
        - Легкость добавления других фигур
        - Вычисление площади фигуры без знания типа фигуры в compile-time
        - Проверку на то, является ли треугольник прямоугольным. ✍️---
'''
from abc import ABC, abstractmethod
import math


class Shape(ABC):   # Абстрактный базовый класс для всех фигур
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):    # Класс для окружности
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Радиус должен быть положительным.')
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):     # Класс для произвольного треугольника
    def __init__(self, a, b, c):
        # Проверка на существование треугольника
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Невозможно построить треугольник")

        self.a = a
        self.b = b
        self.c = c

    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-9

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


def create_shape(shape_type, *args):    # Фабрика для создания объектов разных типов фигур
    shapes = {
        'circle': Circle,
        'triangle': Triangle
    }

    shape_class = shapes.get(shape_type.lower())
    if shape_class:
        return shape_class(*args)
    else:
        raise ValueError(f'Фигура "{shape_type}" не поддерживается')


if __name__ == "__main__":      # Пример использования
    circle = create_shape('circle', 5)
    print(f"Площадь круга: {circle.area():.2f}")

    triangle = create_shape('triangle', 3, 4, 5)
    print(f"Площадь треугольника: {triangle.area():.2f}")
    print(f"Треугольник {('прямоугольный' if triangle.is_right_triangle() else 'не прямоугольный')}")