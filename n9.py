'''

Для заданного интервального выборочного ряда 
(начальное значение min x , шаг h)
проверить гипотезу: закон распределения генеральной совокупности является показательным при уровне значимости
alpha = 0,05.


'''
from my_methods import F, my_mean, my_variance, chi_critical, chi_obvervable
import statistics
from math import sqrt, fabs, e
import numpy as np
from scipy.stats import norm, chi2_contingency
from typing import List, Tuple


alpha = 0.05
min_x = 0
h = 0.2
a0 = min_x
a1 = min_x + h

data = [156, 101, 57, 32, 14, 9, 11, 1, 2, 1, 1]
x = [min_x + h * i for i in range(len(data))]


X = statistics.mean(data)

lamb = 1/X
n: List[float] = []
for i in range(len(x) - 1):
    Pi = sum(data) * (e**(-lamb*x[i])- e**(-lamb*x[i+1]))
    n.append(data[i] * Pi)
    
print(n)


chi: float = sum(list(map(lambda n1, n2: (n1 - n2)**2 / n2, data, n)))
chi_crit: float = 15.5 # по таблице приложения два
print(chi)

if chi > chi_crit:
    print('гипотеза о показательном распределении отклоняется')
    
else:
    print('нет оснований отвергать гипотезу ')