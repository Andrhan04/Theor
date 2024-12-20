'''
Для заданного интервального выборочного ряда 
(начальное значение min x , шаг h)
проверить гипотезу: закон распределения генеральной совокупности является показательным при уровне значимости
alpha = 0,05.
'''
from Function.my_methods import F, my_mean, my_variance, chi_critical, chi_obvervable
import statistics
from math import sqrt, fabs, e
import numpy as np
from scipy.stats import norm, chi2_contingency
from typing import List, Tuple
import scipy.stats as stats

alpha = 0.05
min_x = 0
h = 1.8
data = [206, 98, 64, 29, 14, 5, 3, 1, 0, 1, 1]

def test_exponential(data):
    # Определим параметр λ
    lambda_param = 1 / np.mean(data)
    # Определение интервального распределения
    bins = np.histogram_bin_edges(data, bins='auto')
    observed_freq, _ = np.histogram(data, bins=bins)
    # Теоретические частоты для показательного распределения
    expected_freq = len(data) * (np.diff(bins) * lambda_param * np.exp(-lambda_param * bins[:-1]))
    # Вычисляем значение критерия χ²
    chi_squared = np.sum((observed_freq - expected_freq) ** 2 / expected_freq)
    # Степени свободы: количество интервалов - 1
    df = len(observed_freq) - 1
    critical_value = stats.chi2.ppf(1 - alpha, df)
    print(f'Показательное распределение: χ² = {chi_squared:.4f}, критическое значение = {critical_value:.4f}')
    if(chi_squared > critical_value):
        print('гипотеза отклоняется')
    else:
        print('нет оснований отвергать гипотезу ')
    return chi_squared, critical_value, chi_squared > critical_value


x = [min_x + h * i for i in range(len(data))]
my_data = [data[i] * (x[i+1] - x[i]) for i in range(len(x) - 1)]
print(my_data)
test_exponential(my_data)