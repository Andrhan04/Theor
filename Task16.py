'''
Задание 16. В таблице заданы частоты появлений значений двумерной
дискретной случайной величины
X,Y . При уровне значимости α = 0,05 найти
коэффициент корреляции, проверить его значимость, найти линейные уравнения
регрессии Y на X и X на Y. Построить корреляционное поле и на этом же графике
изобразить обе прямые регрессии.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from Function.my_methods import coeff_correlation, regression_equationYX, search_crit_pearson



X = np.array([50.95, 60.25, 63.24, 73.86, 80.58, 59.09, 76.28, 69.49, 72.36, 63.15,
              70.53, 60.61, 73.96, 83.34, 56.07, 77.28, 57.90, 70.58, 81.27, 81.99])
Y = np.array([65.22, 66.96, 66.45, 67.93, 61.85, 84.83, 68.48, 66.59, 67.08, 68.96,
             53.98, 56.99, 62.89, 70.42, 58.09, 63.98, 61.98, 72.74, 63.48, 52.42])

def main(X=X, Y=Y):
    correlation_coefficient = coeff_correlation(X, Y)
    print(f"Коэффициент корреляции: {correlation_coefficient:.4f}")
    alpha = 0.05
    k = len(X) - 2
    r = search_crit_pearson(alpha=alpha, k=k)

    if correlation_coefficient < r:
        print(f"Коэффициент корреляции значим на уровне α = {alpha}")
    else:
        print(f"Коэффициент корреляции не значим на уровне α = {alpha}")


    # Регрессия Y на X
    slope_Y_on_X, intercept_Y_on_X = regression_equationYX(X, Y)
    # Регрессия X на Y
    slope_X_on_Y, intercept_X_on_Y = regression_equationYX(Y, X)



    print(f"Уравнение регрессии Y на X: Y = {slope_Y_on_X:.4f}  X + {intercept_Y_on_X:.4f}")
    print(f"Уравнение регрессии X на Y: X = {slope_X_on_Y:.4f}  Y + {intercept_X_on_Y:.4f}")


    plt.scatter(X, Y, color='blue', label='Данные')
    plt.plot(X, slope_Y_on_X * X + intercept_Y_on_X, color='red', label='Регрессия Y на X')
    plt.plot(slope_X_on_Y * Y + intercept_X_on_Y, Y, color='green', label='Регрессия X на Y')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Корреляционное поле и регрессии')
    plt.legend()
    plt.grid()
    plt.show()
    