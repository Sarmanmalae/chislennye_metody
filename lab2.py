from math import acos
from math import cos


def metod_dihotomii():
    print("Введите интервал:")
    a, b = float(input()), float(input())
    print("Введите значение погрешности (Эпсилон):")
    e = float(input())
    count = 0

    while abs(b - a) >= e:
        x1 = (a + b) / 2
        fx = x1 * x1 - 2 * cos(x1) + 1
        fa = a * a - 2 * cos(a) + 1
        fb = b * b - 2 * cos(b) + 1
        if fa * fx < 0:
            b = x1
        elif fb * fx < 0:
            a = x1

        count += 1

    print(f"Ответ:\nx1 = {(b + a) / 2}\nx2 = {-1 * (b + a) / 2}\nТочность = {e}\nКол-во итераций = {count}")


def metod_pr_iteraciy():
    print("Введите интервал:")
    a, b = float(input()), float(input())
    print("Введите значение погрешности (Эпсилон):")
    e = float(input())
    count = 1
    x0 = 0
    x1 = (2 * cos(x0) - 1) ** 0.5
    while abs(x1 - x0) >= e:
        x0 = x1
        x1 = (2 * cos(x0) - 1) ** 0.5

        count += 1

    print(f"Ответ:\nx1 = {x1}\nx2 = {-1 * x1}\nТочность = {e}\nКол-во итераций = {count}")


print("Выберите способ:\n1. Метод дихотомии\n2. Метод простых интервалов")
n = int(input())
if n == 1:
    metod_dihotomii()
    print("-----------------------")
    metod_pr_iteraciy()
elif n == 2:
    metod_pr_iteraciy()
    print("-----------------------")
    metod_dihotomii()
