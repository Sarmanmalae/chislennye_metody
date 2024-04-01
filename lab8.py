from math import log, sin, pi


def f(x):
    return sin(x)


def simpson(a, b, n):
    h = (b - a) / n
    summ = f(a) + f(b)
    ans = 1

    for i in range(1, n):
        y = f(a + i * h)
        if i % 2 == 0:
            summ += 2 * y
        else:
            summ += 4 * y

    summ *= h / 3
    return summ, abs(summ - ans)


pred_answer = 0.0
for i in [10, 20, 40, 80, 160]:
    answer = simpson(0, pi/2, i)
    print(
        f"Количество шагов: {i} Значение интеграла: {round(answer[0], 6)} Погрешность: {round(answer[1], 6)} Отношение погрешностей: {pred_answer / answer[1]}")
    pred_answer = answer[1]
