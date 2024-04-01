from math import cos, sin


def f(x):
    return x ** 2 - 2 * cos(x) + 1


def f_(x):
    return 2 * sin(x) + 2 * x


def metod_Newtona():
    print("Введите значение погрешности (Эпсилон):")
    e = float(input())
    count = 1

    x0 = 5
    x1 = x0 - (f(x0) / f_(x0))
    while (f(x1 - e) * f(x1 + e)) > 0:
        x0 = x1
        x1 = x0 - (f(x0) / f_(x0))

        count += 1

    print(f"Ответ:\nx1 = {x1}\nx2 = {-1 * x1}\nТочность = {e}\nКол-во итераций = {count}")


def metod_hord():
    print("Введите интервал:")
    a, b = float(input()), float(input())
    print("Введите значение погрешности (Эпсилон):")
    e = float(input())
    count = 0
    x1 = 0
    while (f(x1 - e) * f(x1 + e)) > 0:
        x1 = a - (((b - a) * f(a)) / (f(b) - f(a)))
        if f(a) * f(x1) < 0:
            b = x1
        elif f(b) * f(x1) < 0:
            a = x1

        count += 1

    print(f"Ответ:\nx1 = {x1}\nx2 = {-1 * x1}\nТочность = {e}\nКол-во итераций = {count}")


print("Выберите способ:\n1. Метод Ньютона\n2. Метод хорд")
n = int(input())
if n == 1:
    metod_Newtona()
    print("-----------------------")
    metod_hord()
elif n == 2:
    metod_hord()
    print("-----------------------")
    metod_Newtona()
