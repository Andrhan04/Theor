import scipy
import numpy as np
import statistics
from typing import List
data = scipy.stats.norm.cdf(np.linspace(0,1,101)) - 0.5

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
    data = {'x' : data_x, 'p' : data_p}
    X = my_mean(data_x=data_x, data_p=data_p)

    S = my_variance(data_x=data_x, data_p=data_p)
    delta = sqrt(S)

    a_ = X - sqrt(3)*delta
    b_ = X + sqrt(3)*delta

    fx = 1 / fabs(a_ - b_)
    
    n = [None] * len(data_p)
    
    n[0] = n_ * (data_x[0] - a_) * fx
    for i in range(1, len(n) - 1):
        n[i] = n_ * (data_x[i] - data_x[i-1]) * fx

    n[-1] = n_ * (b_ - data_x[-2]) * fx
    
    data_diff = [((data_p[i] - n[i]) ** 2) / n[i] for i in range(len(data_p))]
    
    return sum(data_diff)