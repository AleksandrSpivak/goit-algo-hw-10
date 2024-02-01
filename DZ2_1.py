import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції
def f(x):
    return x**3


# Перевіряє, чи знаходиться точка (x, y) під кривою у = х ** 3
def is_inside(x, y):
    return y <= x**3


# Межі інтегруваня
a = 1  # Нижня межа інтегрування
b = 2  # Верхня межа інтегрування

# Розміри прямокутника
c = 1  # ширина прямокутника
d = 8  # висота прямокутника

TEST_SIZE = 1_000_000  # Кількість тестових точок

# Створення діапазону значень для x
x = np.linspace(-0.2, 2.2, 400)
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
ax.set_title("Графік інтегрування f(x) = x^3 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()

result, error = spi.quad(f, a, b)
print(f"Інтеграл, обчислений функцією quad з бібліотеки scipy = {result:.6f}")

# Генерація випадкових точок
counter = 0
for _ in range(TEST_SIZE):
    point = (random.uniform(1, 1 + c), random.uniform(0, d))
    if is_inside(point[0], point[1]):
        counter += 1

# Теоретична площа трикутника та площа, обчислена методом Монте-Карло
S = 1 / 4 * (2**4) - 1 / 4 * (1**4)  # Теоретична площа
# Площа за методом Монте-Карло
Sm = counter / TEST_SIZE * (c * d)

# Виведення результатів
print(f"Теоретична площа фігури: {S},\nПлоща фігури за методом Монте-Карло: {Sm:.6f}")
print(
    f"Кількість точок всередині фігури: {counter:_}, загальна кількість точок: {TEST_SIZE:_}"
)
