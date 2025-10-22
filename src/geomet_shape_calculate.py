from math import pi, sin, cos, sqrt, isclose
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError('Положительный радиус.')
        self.radius = radius

    def area(self) -> float:
            return pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if not self.is_valid_triangle(a, b, c):
            raise ValueError('Недопустимое значение сторон.')
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_valid_triangle(self, a: float, b: float, c: float) -> bool:
        return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

    def is_right_angled(self, tolerance=1e-10) -> bool:
        sides = sorted([self.a, self.b, self.c])
        #Проверяем, что квадрат гипотенузы примерно равен сумме квадратов катетов
        return isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, abs_tol=tolerance) #sides[0]2+sides[1]2≈sides[2]2

'''
Что можно улучшить:

 * Добавить больше фигур
 
'''