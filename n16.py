import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from my_methods import coeff_correlation, regression_equationYX, search_crit_pearson



X = np.array([90.20, 113.0, 100.2, 103.2, 95.15, 108.9, 90.42, 99.51, 89.39, 
              92.10, 92.62, 102.0, 87.23, 93.59, 94.61, 92.57, 101.7, 
              104.4, 102.4, 97.14])
Y = np.array([93.14, 94.78, 107.9, 101.6, 104.4, 98.65, 95.37, 97.28, 
              86.80, 90.39, 86.52, 99.84, 93.84, 107.8, 89.01, 98.11, 
              100.3, 90.68, 96.36, 111.9])

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
    
