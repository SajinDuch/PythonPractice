import unittest     # Импортируем встроенный модуль unittest для написания и запуска тестов
from unittest.mock import patch     # Импортируем patch — инструмент для замены объектов (например, стандартного вывода или ввода) во время теста
from math import sqrt, pi      # Импортируем из math константу pi и функцию sqrt (квадратный корень), чтобы рассчитывать ожидаемые площади фигур
from geomet_shape_calculate import Circle, Triangle, Shape     # Импортируем классы фигур из вашего модуля geom_shapes, чтобы создавать экземпляры и тестировать их методы
import io # Импортируем модуль io, который предоставляет различные классы для работы с потоками,
            # здесь используем io.StringIO — "поток" для хранения строк в памяти, чтобы перехватывать вывод

# 📌 --- Класс тестов для круга ---
class TestSuite1_Circle(unittest.TestCase):
    # Класс-наследник unittest.TestCase — набор тестов для Circle

    def test_01_area(self):    # ✅ Тест проверяет правильность расчёта площади круга
        c = Circle(5)     # Создаём объект Circle с радиусом 5
        expected_area = pi * 5 ** 2     #Вычисляем ожидаемую площадь вручную (πr²)
        self.assertAlmostEqual(c.area(), expected_area)     #Проверяем, что метод area() возвращает значение, близкое к ожидаемому (с учётом погрешности)

    def test_02_invalid_radius(self):      # ❌ Тест проверяет, что при некорректном радиусе возбуждается исключение
        with self.assertRaises(ValueError):     # Проверяем, что создание круга с радиусом 0 вызывает ValueError
            Circle(0)

        with self.assertRaises(ValueError):     # Проверяем, что создание круга с отрицательным радиусом вызывает ValueError
            Circle(-1)

# 📌 --- Класс тестов для треугольника ---
class TestSuite2_Triangle(unittest.TestCase):      # Набор тестов для класса Triangle

    def test_01_valid_triangle_area(self):      # ✅ Проверяем правильность вычисления площади для валидного треугольника

        t = Triangle(3, 4, 5)      # Создаём треугольник со сторонами 3, 4, 5
        s = (3 + 4 + 5) / 2     # Полупериметр (формула Герона)
        expected_area = sqrt(s * (s - 3) * (s - 4) * (s - 5))     # Вычисляем ожидаемую площадь по формуле Герона
        self.assertAlmostEqual(t.area(), expected_area)

    def test_02_invalid_triangle(self):     # ❌ Проверяем, что некорректные стороны треугольника вызывают ошибку
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)      # стороны не могут составить треугольник


# 📌 --- Класс тестов для функции print_area из run.py ---
class TestSuite3_PrintArea(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)      # 📣 Декоратор, который подменяет sys.stdout на объект StringIO,
                                                                # чтобы перехватить всё, что выводится в консоль внутри теста

    def test_01_print_area_circle(self, mock_stdout):       # Тестируем вывод площади круга функцией print_area
        c = Circle(5)
        from run import print_area      # Импортируем функцию print_area из модуля run (во время теста)

        print_area(c)     # Вызываем функцию с объектом круга

        output = mock_stdout.getvalue().strip()     # Получаем захваченный вывод из mock_stdout, удаляем пробельные символы по краям

        expected_area = pi * 5 ** 2     # Вычисляем ожидаемую площадь

        self.assertIn("круга", output)      # Проверяем, что в выводе есть слово "круга" (русское название фигуры)

        self.assertIn(f"{expected_area:.2f}", output)     # Проверяем, что площадь выведена с двумя знаками после запятой

    @patch('sys.stdout', new_callable=io.StringIO)      # 📣 Декоратор, который подменяет sys.stdout на объект StringIO,
                                                                # чтобы перехватить всё, что выводится в консоль внутри теста

    def test_02_print_area_triangle(self, mock_stdout):       # Тестируем вывод площади треугольника функцией print_area
        t = Triangle(3, 4, 5)
        from run import print_area      # Импортируем функцию print_area из модуля run (во время теста)

        print_area(t)       # Вызываем функцию с объектом треугольника

        output = mock_stdout.getvalue().strip()     # Получаем захваченный вывод из mock_stdout, удаляем пробельные символы по краям

        s = (3 + 4 + 5) / 2     # Вычисляем ожидаемую площадь
        expected_area = sqrt(s * (s - 3) * (s - 4) * (s - 5))

        self.assertIn("треугольника", output)       # Проверяем, что в выводе есть слово "треугольника" (русское название фигуры)

        self.assertIn(f"{expected_area:.2f}", output)       # Проверяем, что площадь выведена с двумя знаками после запятой

# 📌 --- Точка входа для запуска тестов ---
if __name__ == '__main__':
    unittest.main()     #Запускает все тесты, когда этот файл запускается как основная программа

'''
Что можно улучшить:

Можно добавить больше граничных случаев (например, очень маленькие/большие значения сторон).
В тестах лучше явно указывать, что исключение должно иметь определённое сообщение (если это важно).
'''