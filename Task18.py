'''
Задание 18. 
Используя метод наименьших квадратов, найти уравнение прямой по экспериментальным данным, и построить эту прямую. 
Сравнить полученный результат с результатом расчета в пакете «Анализ данных».
'''
import numpy as np
import matplotlib.pyplot as plt
from Function.my_methods import regression_equationYX

X = np.array([-2,-1,0, 1, 4, 5,6, 7, 8, 10])
Y = np.array([-8, -5, -3, 1, 10, 15, 16, 20, 22, 26])

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