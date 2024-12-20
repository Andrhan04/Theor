import numpy as np
import matplotlib.pyplot as plt
from my_methods import regression_equationYX

X = np.array([-5, -4, -2, 0, 1, 2, 4, 6, 8, 9])
Y = np.array([-24, -18, -9, 1, 7, 13, 21, 32, 41, 46])
"""
Используя метод наименьших квадратов, найти уравнение прямой по экспериментальным данным, и построить эту прямую.
Сравнить полученный результат с результатом расчета в пакете «Анализ данных».
"""
def main():
    a, b = regression_equationYX(X, Y)#используя свой метод

    print(f"Уравнение прямой своим методом: y = {a:.4f}x + {b:.4f}")
    slope_Y_on_X, intercept_Y_on_X = np.polyfit(X, Y, 1)


    print(f"Уравнение c помощью готовых методов: Y = {slope_Y_on_X:.4f}  X + {intercept_Y_on_X:.4f}")

    plt.scatter(X, Y, color='blue', label='Экспериментальные данные')
    plt.plot(X, a * X + b, color='red', label='Уравнение прямой')
    plt.plot(X, float(slope_Y_on_X) * X + float(intercept_Y_on_X), color='green', label='Уравнение прямой готовым методом')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Построение уравнения прямой методом наименьших квадратов')
    plt.legend()
    plt.grid()
    plt.show()
    
main()