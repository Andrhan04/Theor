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
from scipy import stats
from typing import List, Tuple


alpha = 0.05
min_x = 0
h = 0.2
a0 = min_x
a1 = min_x + h

data = [156, 101, 57, 32, 14, 9, 11, 1, 2, 1, 1]
x = [min_x + h * i for i in range(len(data)+1)]
data1 = [data[i] * (x[i+1] - x[i]) for i in range(len(x) - 1)]

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
    return chi_squared, critical_value, chi_squared > critical_value

test_exponential(data1)