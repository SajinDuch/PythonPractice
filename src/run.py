from geomet_shape_calculate import Circle, Triangle, Shape

def print_area(shape: Shape):
    print(f"Area: {type(shape).__name__}: {shape.area()}")

def main():     # Создаем круг и треугольник
    circle = Circle(5)
    triangle = Triangle(5,4,8)

    print_area(circle)
    print_area(triangle)

    if triangle.is_right_angled():     # Проверка прямоугольности треугольника
        print("Треугольник прямоугольный")
    else:
        print("Треугольник не является прямоугольным")

if __name__ == '__main__':
    main()