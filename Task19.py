'''
Задание 19. 
Используя метод наименьших квадратов, найти параметры линейной, квадратичной и показательной зависимостей аппроксимирующей функции. 
Определить, какая из функций является лучшим приближением зависимости между х и у.

'''
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from Function.my_methods import regression_equationYX, coeff_correlation

np.random.seed(0)  
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([0.1, 1.5, 2.8, 8.2, 20.2, 55.4, 127.5, 223, 497.6, 980])

# Метод для линейной зависимости
def linear_fit(x, y):
    a, b = regression_equationYX(x, y)
    return float(a), float(b)

# Метод для квадратичной зависимости
def quadratic_fit(x, y):
    A = np.vstack([x**2, x, np.ones(len(x))]).T
    params = inv(A.T @ A) @ A.T @ y
    return params


def exponential_fit(x, y):
        
    log_y = np.log(y)
    a, b = linear_fit(x, log_y)
    return a, b

def compute_r_squared(y, y_pred):
    ss_tot = np.sum((y - np.mean(y)) ** 2)  # Общая сумма квадратов
    ss_res = np.sum((y - y_pred) ** 2)      # Сумма квадратов ошибок
    r_squared = 1 - (ss_res / ss_tot)       # Коэффициент детерминации
    return r_squared


def main(x=x, y=y):
    linear_params = linear_fit(x, y)
    quadratic_params = quadratic_fit(x, y)
    exponential_params = exponential_fit(x, y)

    #предсказанные значение
    y_linear_pred = linear_params[0] * x + linear_params[1]
    y_quadratic_pred = quadratic_params[0] * x**2 + quadratic_params[1] * x + quadratic_params[2]
    y_exponential_pred = exponential_params[0] * np.exp((exponential_params[1]) * x)

    # R^2 для каждой модели
    r2_linear = compute_r_squared(y, y_linear_pred)
    r2_quadratic = compute_r_squared(y, y_quadratic_pred)
    r2_exponential = compute_r_squared(y, y_exponential_pred)

    print(f'Линейные параметры: a = {linear_params[0]:.4f}, b = {linear_params[1]:.4f}')
    print(f'Квадратичные параметры: a = {quadratic_params[0]:.4f}, b = {quadratic_params[1]:.4f}, c = {quadratic_params[2]:.4f}')
    print(f'Показательные параметры: a = {exponential_params[0]:.4f}, b = {exponential_params[1]:.4f}')
    print('----')
    print(r2_linear)
    print(r2_quadratic)
    print(r2_exponential)
    plt.figure(figsize=(12, 8))
    plt.scatter(x, y, label='Данные', color='black', s=10)

    plt.plot(x, linear_params[0]*x + linear_params[1], 'r-', label='Линейная аппроксимация')

    x_quad = np.linspace(1, 10, 100)
    plt.plot(x_quad, quadratic_params[0]*x_quad**2 + quadratic_params[1]*x_quad + quadratic_params[2], 'g-', label='Квадратичная аппроксимация')


    plt.plot(x, exponential_params[0] * np.exp(exponential_params[1] * x), 'b-', label='Показательная аппроксимация')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Аппроксимация зависимостей')
    plt.legend()
    plt.grid()
    plt.show()