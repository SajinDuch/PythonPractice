from geomet_shape_calculate import Circle, Triangle, Shape

def print_area(shape: Shape):
    name_map = {
        'Circle': 'круга',
        'Triangle': 'треугольника'
    }
    shape_name = name_map.get(type(shape).__name__, type(shape).__name__)
    print(f"Площадь {shape_name}: {shape.area():.2f}")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Введите положительное число.")
                continue
            return value
        except ValueError:
            print("Некорректный ввод. Введите число.")

def main():
    print("Создание круга")
    radius = get_positive_float("Введите радиус круга: ")
    circle = Circle(radius)

    print("Создание треугольника")
    a = get_positive_float("Введите сторону a: ")
    b = get_positive_float("Введите сторону b: ")
    c = get_positive_float("Введите сторону c: ")

    try:
        triangle = Triangle(a, b, c)
    except ValueError as e:
        print(f"Ошибка создания треугольника: {e}")
        return

    print_area(circle)
    print_area(triangle)

    if triangle.is_right_angled():
        print("Треугольник прямоугольный.")
    else:
        print("Треугольник не является прямоугольным.")

if __name__ == '__main__':
    main()