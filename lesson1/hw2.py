print("Для вычисления квадратного уравнения введите числа")
a = input("Введите первое число: ")
a = int(a)
b = input("Введите второе число: ")
b = int(b)
c = input("Введите третье число: ")
c = int(c)
d = b * b - 4 * a * c
if d < 0:
    print("Дискриминант = ", d)
    print("Дискриминант < 0, в квадратном уравнении нет корней!")
elif d > 0:
    x1 = ((-1 * b) + (d ** .5)) / (2 * a)
    x2 = ((-1 * b) - (d ** .5)) / (2 * a)
    print("Дискриминант = ", d)
    print("Корень x1 = ", x1)
    print("Корень x2 = ", x2)
else:
    x1 = ((-1 * b) + (d ** .5)) / (2 * a)
    print("Дискриминант = 0, в квадратном уравнении будет 1 корень!")
    print("Корень x1 = ", x1)
