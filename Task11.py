'''
Задание 11. По данным выборки проверить с помощью критерия Пирсона при уровне значимости alpha гипотезу:
    а) о показательном;
    б) равномерном;
    в) нормальном законе распределения генеральной совокупности.
В ответе привести:
    1) выбранную гипотезу о виде закона распределения;
    2) вычисленное значение критерия;
    3) критическое значение;
    4) вывод о принятии или не принятии гипотезы.
'''
from collections import Counter
from Function.my_methods import chi_critical, chi_obvervable
import numpy as np
import scipy.stats as stats
# Данные выборки
data = [21.8, 2.4, 13.8, 7.0, 21.8, 19.2, 14.9, 20.5, 18.2, 16.3, 16.8, 16.4,
        17.6, 30.2, 0.2, 22.6, 12.8, 4.6, 8.5, 15.6, 16.8, 27.7, 11.2, 5.2, 14.0,
        12.7, 7.1, 15.0, 13.4, 14.6, 11.1, 9.6, 12.1, 1.1, 20.9, 16.1, 10.6,
        19.0, 11.9, 0.6, 22.1, 16.5, 29.0, 6.3, 14.1, 27.9, 8.3, 12.6, 16.4,
        6.8, 17.4, 2.6, 7.9, 9.0, 16.8, 15.1, 13.2, 13.2, 9.9, 27.2, 15.8, 17.3,
        12.4, 25.2, 13.5, 4.5, 5.3, 21.9, 20.4, 7.5, 26.0, 12.8, 21.2, 23.0,
        7.9, 22.4, 12.1, 15.3, 4.8, 12.8, 25.3, 18.6, 14.0, 9.9, 9.1, -0.6, 16.7,
        9.5, 14.6, 16.4, 14.6, 13.3, 13.1, 15.8, 20.5, 6.4, 24.7, 7.6, 9.1, 11.1]


# Далее приводим пример для каждой гипотезы

alpha = 0.05  # уровень значимости

# 1. Проверка на показательное распределение
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

# 2. Проверка на равномерное распределение
def test_uniform(data):
    # Определение диапазона данных
    min_val, max_val = np.min(data), np.max(data)
    bins = np.linspace(min_val, max_val, 6)  # 5 интервалов для равномерного распределения
    observed_freq, _ = np.histogram(data, bins=bins)
    
    # Теоретические частоты для равномерного распределения
    expected_freq = len(data) / len(observed_freq) * np.ones_like(observed_freq)

    # Вычисляем значение критерия χ²
    chi_squared = np.sum((observed_freq - expected_freq) ** 2 / expected_freq)
    
    # Степени свободы
    df = len(observed_freq) - 1
    critical_value = stats.chi2.ppf(1 - alpha, df)
    
    print(f'Равномерное распределение: χ² = {chi_squared:.4f}, критическое значение = {critical_value:.4f}')
    if(chi_squared > critical_value):
        print('гипотеза отклоняется')
    else:
        print('нет оснований отвергать гипотезу ')
    return chi_squared, critical_value, chi_squared > critical_value

# 3. Проверка на нормальное распределение
def test_normal(data):
    # Определение параметров нормального распределения
    mu, sigma = np.mean(data), np.std(data)
    
    # Определение интервального распределения
    bins = np.histogram_bin_edges(data, bins='auto')
    observed_freq, _ = np.histogram(data, bins=bins)
    
    # Теоретические частоты для нормального распределения
    expected_freq = len(data) * (stats.norm.cdf(bins[1:], mu, sigma) - stats.norm.cdf(bins[:-1], mu, sigma))

    # Вычисляем значение критерия χ²
    chi_squared = np.sum((observed_freq - expected_freq) ** 2 / expected_freq)
    
    # Степени свободы
    df = len(observed_freq) - 1
    critical_value = stats.chi2.ppf(1 - alpha, df)
    
    print(f'Нормальное распределение: χ² = {chi_squared:.4f}, критическое значение = {critical_value:.4f}')
    if(chi_squared > critical_value):
        print('гипотеза отклоняется')
    else:
        print('нет оснований отвергать гипотезу ')
    return chi_squared, critical_value, chi_squared > critical_value

# Запуск тестов
test_exponential(data)
test_uniform(data)
test_normal(data)