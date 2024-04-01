from math import log


def f(x):
    return ((1 + 5 * log(x)) ** 0.5) / x


def f_(x):
    return (-10 * log(x) + 3) / (2 * x ** 2 * (5 * log(x) + 1) ** 0.5)


def rect(a, b, n):
    h = (b - a) / n
    summ = 0
    e = ((abs(f_(b)) * h) / 2) * (b - a)

    for i in range(n):
        summ += f(a + i * h) * h

    return summ, e


print(rect(1, 100, 10))
print(rect(1, 100, 20))
print(rect(1, 100, 30))
print(rect(1, 100, 40))
print(rect(1, 100, 50))

