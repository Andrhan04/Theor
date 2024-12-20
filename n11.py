

import numpy as np
import scipy.stats as stats

# Данные выборки
data = np.array([
    35.1, 46.7, 23.9, 50.5, 32.3, 32.5, 32.7, 21.5, 33.1, 34.0, 42.4, 53.6,
    34.8, 18.7, 25.7, 29.1, 18.4, 38.8, 23.6, 19.5, 22.7, 26.8, 54.1, 47.4,
    42.0, 24.0, 35.9, 58.1, 45.1, 5.8, 27.6, 25.4, 40.8, 41.5, 18.3, 36.5,
    30.3, 29.5, 30.0, 58.1, 43.2, 28.1, 17.4, 30.4, 45.9, 42.6, 33.7, 42.8,
    32.5, 21.4, 30.0, 45.8, 29.2, 42.9, 18.9, 26.2, 23.3, 42.8, 42.6, 35.8,
    33.5, 38.8, 38.9, 42.2, 32.0, 32.9, 29.2, 42.1, 28.3, 50.2, 46.5, 32.4,
    16.2, 36.8, 33.5, 31.6, 23.0, 46.6, 18.7, 30.4, 29.4, 21.8, 36.1, 34.2,
    39.5, 32.9, 33.5, 24.1, 6.0, 17.8, 21.1, 42.6, 30.4, 29.1, 52.3, 37.4,
    39.9, 39.1, 37.5, 41.6
])

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
    if chi_squared > critical_value:
        print('гипотеза о Показательном распределении отвергнута')
    else:
        print('нет оснований отвергать гипотезу Показательного распределения')
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
    if chi_squared > critical_value:
        print('гипотеза о равномерном распределении отвергнута')
    else:
        print('нет оснований отвергать гипотезу равномерного распределения')
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
    if chi_squared > critical_value:
        print('гипотеза о нормальном распределении отвергнута')
    else:
        print('нет оснований отвергать гипотезу нормального распределения')
    return chi_squared, critical_value, chi_squared > critical_value

# Запуск тестов
test_exponential(data)
test_uniform(data)
test_normal(data)