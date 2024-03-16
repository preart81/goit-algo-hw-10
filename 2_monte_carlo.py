"""
Обчислення визначеного інтеграла методом Монте-Карло

Порівння результатів розрахунків методом Монте-Карло та обчисленого інтегралу за
допомогою spi.quad()"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції та меж інтегрування

# Межі інтегрування
a = 2  # Нижня межа
b = 32  # Верхня межа

# Функція для інтегрування
func = np.log2


def f(x):
    return func(x)


def show_grafic(a, b, text=""):
    d = (b - a) * 0.1

    # Створення діапазону значень для x
    x = np.linspace(0, b + d, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, "r", linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(
        f"Графік інтегрування f(x) = {func.__name__}(x) від {str(a)} до {str(b)}"
    )

    # Додавання багаторядкового тексту під графіком
    # ax.text(0, -1, text, ha="left", va="bottom", fontsize=10)
    fig.text(0.7, 0.3, text, ha="right", va="center", fontsize=10)

    plt.grid()
    plt.show()


def monte_carlo(a, b, n: int = 1000_000):
    """
    Обрахунок інтеграла методом Монте-Карло

    Параметри:
        a - нижня межа
        b - верхня межа
        n - кількість точок для обчислення інтеграла

    """
    # Генерація набору точок для обчислення інтеграла
    x_rnd = np.random.uniform(a, b, n)
    y_rnd = np.random.uniform(0, f(b), n)

    # Кількість точок, що знаходяться під кривою
    uder_curve_points = sum(y_rnd <= f(x_rnd))

    # Площа описаного прямокутника (наш інтеграл знаходиться всередині цього прямокутника)
    area_rectangle = (b - a) * f(b)

    # Обчислення інтегралу
    # як пропорцію кількості точок, що знаходяться під кривою до загальної к-ті точок
    # помножену на площу описаного прямокутника

    integral = area_rectangle * uder_curve_points / n

    return integral


print(f"Обчислення інтегралу різнми методами:")
print(f"функція: {func.__name__}")
print(f"межі інтегрування: {a} - {b}")
print()
s_monte_carlo = monte_carlo(a, b)
print(f"метод Монте-Карло: S={s_monte_carlo:.4f}")

# Обчислимо інтеграл за допомогою spi.quad()
result, error = spi.quad(func, a, b)
print(f"функція quad():    S={result:.4f}, похибка = {error}")

txt = f"Монте-Карло: S={s_monte_carlo:.4f}"
txt += "\n"
txt += f"spi.quad(): S={result:.4f}"
show_grafic(a, b, txt)
