# Практическое задание № 1 (вариант 12)
# Построение графика функции y = log₃(x)

import numpy as np
import matplotlib.pyplot as plt

# Задаём диапазон значений x от -5 до 15 с шагом 1.4
x_values = np.arange(-5, 15, 1.4)

# Вычисляем значения y = log base 3 (x), исключая некорректные x ≤ 0
x_valid = x_values[x_values > 0]
y_values = np.log(x_valid) / np.log(3)  # логарифм по основанию 3

# Строим график
plt.plot(x_valid, y_values, color='red', label='y = log₃(x)')
plt.title('График функции y = log₃(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Сохраняем результат в файл
plt.savefig("graph_log3.png")
print("График сохранён в файл graph_log3.png")
