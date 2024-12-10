import scipy
import numpy as np
import statistics
from typing import List

import scipy.optimize
data = scipy.stats.norm.cdf(np.linspace(0,1,101)) - 0.5

import scipy.linalg
from scipy.stats import chi2


from math import sqrt, fabs


d = {}
n = 0
for i in data:
    d[n] = round(float(i), 4)
    n = round(n+0.01, 3)
    
    
def F(x):
    print(x)
    return d[x]




def my_mean(data_x, data_p):
    data = []
    for i in range(len(data_x)):
        data += data_p[i] * [data_x[i]]
    return statistics.mean(data)


def my_variance(data_x, data_p):
    data = []
    for i in range(len(data_x)):
        data += data_p[i] * [data_x[i]]
    return statistics.variance(data)




def chi_critical(k: int = 5,  alpha : float = 0.01):
    
    alpha_levels = [0.99, 0.95, 0.1, 0.05, 0.025, 0.01]

    # Задаем максимальное количество степеней свободы
    max_df = max(20, k+7)

    # Создаем словарь для хранения критических точек
    critical_values = {}

    # Вычисляем критические точки
    for df in range(1, max_df + 1):
        critical_values[df] = {alpha: chi2.ppf(1 - alpha, df) for alpha in alpha_levels}
        
    return critical_values[k][alpha]


def chi_obvervable(data_p, data_x, alpha):
    n_ = sum(data_p)
    my_mean(data_x=data_x, data_p=data_p)
    X = my_mean(data_x=data_x, data_p=data_p)

    S = my_variance(data_x=data_x, data_p=data_p)
    delta = sqrt(S)

    a_ = X - sqrt(3)*delta
    b_ = X + sqrt(3)*delta

    fx = 1 / abs(a_ - b_)
    
    n = [None] * len(data_p)
    
    n[0] = n_ * (data_x[0] - a_) * fx
    for i in range(1, len(n) - 1):
        n[i] = n_ * (data_x[i] - data_x[i-1]) * fx

    n[-1] = n_ * (b_ - data_x[-2]) * fx
    
    data_diff = [((data_p[i] - n[i]) ** 2) / n[i] for i in range(len(data_p))]
    
    return sum(data_diff)


def critical_pearson_correlation(level_of_significance, n):
    """Вычисление критического значения коэффициента корреляции Пирсона."""
    df = n - 2
    t_critical = scipy.stats.t.ppf(1 - level_of_significance / 2, df)
    r_critical = t_critical / np.sqrt(t_critical**2 + df)
    return r_critical

def search_crit_pearson(alpha: float, k: int) -> float:
    levels_of_significance = [0.1, 0.05, 0.01]

    sample_sizes = range(5, 31)


    data = {}
    for level in levels_of_significance:
        critical_values = []
        for n in sample_sizes:
            r_critical = critical_pearson_correlation(level, n)
            critical_values.append(round(float(r_critical), 3))
            #print(critical_values)
        data[f'{level}'] = critical_values
    return data[str(alpha)][k-5]



def regression_equationYX(X: List, Y: List) -> str:
    n = len(X)
    Xsum: float = sum(X)
    Ysum: float = sum(Y)
    XY: List[float] = list(map(lambda x, y: x*y, X, Y))
    XYsum: float = sum(XY)
    Xsqr: List[float] = list(map(lambda x: x**2, X))
    Xsqrsum: float = sum(Xsqr)
    Ysqr: List[float] = list(map(lambda y: y**2, Y))
    Ysqrsum: float = sum(Ysqr)

    # print(f"X: {list(map(lambda x: round(x, 3), X))}\nsum X = {Xsum}")
    # print(f"Y: {list(map(lambda y: round(y, 3), Y))}\nsum Y = {Ysum}")
    # print(f"X*Y: {list(map(lambda xy: round(xy, 3), XY))}\nsum X*Y = {XYsum}")
    # print(f"X^2: {list(map(lambda xx: round(xx, 3), Xsqr))}\nsum X^2 = {Xsqr}")
    # print(f"Y^2: {list(map(lambda yy: round(yy, 3), Ysqr))}\nsum Y^2 = {Ysqr}")
    
    sys_equations_A = [[Xsqrsum, Xsum], [Xsum, n]]
    sys_equations_B = [XYsum, Ysum]
    a, b = list(map(lambda x: x, scipy.linalg.solve(sys_equations_A, sys_equations_B)))
    # print(f'Система: a*{sys_equations_A[0][0]:.3f} + b*{sys_equations_A[0][1]:.3f} = {sys_equations_B[0]:.3f}')
    # print(f'Система: a*{sys_equations_A[1][0]:.3f} + b*{sys_equations_A[1][1]:.3f} = {sys_equations_B[1]:.3f}')
    print(f"Корни системы: a = {a:.6f}, b = {b:.6f}")
    return (a, b)
    

def coeff_correlation(X: List[float], Y: List[float]) -> float:
    n: int = len(X)
    xy_ = sum(map(lambda x, y: x*y, X, Y)) / n
    x_ = sum(X) / n
    y_ = sum(Y) / n
    
    sigmaX = sqrt(sum(list(map(lambda x: x*x, X)))/n - x_**2)
    sigmaY = sqrt(sum(list(map(lambda y: y*y, Y)))/n - y_**2)
    
    print(sigmaX, sigmaY)
    coeff = (xy_ - x_ * y_) / (sigmaX * sigmaY)
    print(coeff)
    print(coeff * sigmaX / sigmaY)
    return coeff



def main():
    # coeff_correlation(# for test
        # [12, 9, 8, 14, 15, 11, 10, 15],
        # [42, 107, 100, 60, 78, 79, 90, 54]
    # ) 
    X = [90.20, 113.0, 100.2, 103.2, 95.15, 108.9, 90.42, 99.51, 89.39, 
              92.10, 92.62, 102.0, 87.23, 93.59, 94.61, 92.57, 101.7, 
              104.4, 102.4, 97.14]
    Y = [93.14, 94.78, 107.9, 101.6, 104.4, 98.65, 95.37, 97.28, 
              86.80, 90.39, 86.52, 99.84, 93.84, 107.8, 89.01, 98.11, 
                100.3, 90.68, 96.36, 111.9]
    coeff_correlation(X, Y)

if __name__ == '__main__':
    main()