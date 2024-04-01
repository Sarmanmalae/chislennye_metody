from math import log, sin, pi


def f(x):
    return sin(x)


def trapecia(a, b, n):
    h = (b - a) / n
    summ = (f(a) + f(b))/2
    e = 1

    for j in range(1, n):
        summ += f(a + h * j)

    summ *= h

    return [summ, abs(summ - e)]


pred_answer = 0.0
for i in [10, 20, 40, 80, 160]:
    answer = trapecia(0, pi/2, i)
    print(
        f"Количество шагов: {i} Значение интеграла: {round(answer[0], 6)} Погрешность: {round(answer[1], 6)} Отношение погрешностей: {pred_answer / answer[1]}")
    pred_answer = answer[1]
