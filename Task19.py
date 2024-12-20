import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

np.random.seed(0)  
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([0.1, 1.5, 2.8, 8.2, 20.2, 55.4, 127.5, 223, 497.6, 980])
"""
Используя метод наименьших квадратов, найти параметры линейной, квадратичной и показательной зависимостей аппроксимирующей функции. 
Определить, какая из функций является лучшим приближением зависимости
между х и у.

"""
#import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Данные
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0])
y = np.array([1.1, 2.6, 2.7, 3.0, 4.1, 4.6, 4.7, 3.4, 4.8, 5.1, 5.7, 5.2, 5.6])

# Определение моделей
def linear_model(x, a0, a1):
    return a0 + a1 * x

def quadratic_model(x, a0, a1, a2):
    return a0 + a1 * x + a2 * x**2

def exponential_model(x, a0, a1):
    return a0 * np.exp(a1 * x)

# Подбор параметров
linear_params, _ = curve_fit(linear_model, x, y)
quadratic_params, _ = curve_fit(quadratic_model, x, y)
exponential_params, _ = curve_fit(exponential_model, x, y, p0=(1, 0.1))

# Вычисление значений для моделей
y_linear = linear_model(x, *linear_params)
y_quadratic = quadratic_model(x, *quadratic_params)
y_exponential = exponential_model(x, *exponential_params)

# Вычисление R² для каждой модели
def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)

r2_linear = r_squared(y, y_linear)
r2_quadratic = r_squared(y, y_quadratic)
r2_exponential = r_squared(y, y_exponential)

# Результаты
print(f"Линейная модель: параметры = {linear_params}, R² = {r2_linear:.4f}")
print(f"Квадратичная модель: параметры = {quadratic_params}, R² = {r2_quadratic:.4f}")
print(f"Показательная модель: параметры = {exponential_params}, R² = {r2_exponential:.4f}")

# Визуализация
plt.scatter(x, y, label='Данные', color='black')
plt.plot(x, y_linear, label='Линейная модель', color='blue')
plt.plot(x, y_quadratic, label='Квадратичная модель', color='green')
plt.plot(x, y_exponential, label='Показательная модель', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Аппроксимация зависимостей')
plt.show()