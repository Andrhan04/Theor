import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Данные
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([0.1, 1.5, 2.8, 8.2, 20.2, 55.4, 127.5, 223, 497.6, 980])

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
plt.scatter(x, y, label='Данные', color='red')
plt.plot(x, y_linear, label='Линейная модель', color='blue')
plt.plot(x, y_quadratic, label='Квадратичная модель', color='green')
plt.plot(x, y_exponential, label='Показательная модель', color='orange')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Аппроксимация зависимостей')
plt.show()