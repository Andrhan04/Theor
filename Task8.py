import numpy as np
from scipy.stats import norm, chi2_contingency
from Function.my_methods import chi_critical
# Данные
data = [5, 7, 21, 66, 84, 90, 70, 20, 5, 3]
'''
Для заданного интервального выборочного ряда 
(начальное значение min x , шаг h)
проверить гипотезу: закон распределения генеральной совокупности является нормальным при уровне значимости
alpha = 0,05.

'''
# Параметры
min_x = 10.1
h = 2.0
alpha = 0.1
n_intervals = int((max(data) - min_x) / h) + 1

# Границы интервалов
bins = np.linspace(min_x, min_x + n_intervals * h, n_intervals + 1)

# Наблюдаемые частоты
observed_frequencies, _ = np.histogram(data, bins=bins)

# Среднее и стандартное отклонение
mean = np.mean(data)
std_dev = np.std(data)

# Ожидаемые частоты для нормального распределения
expected_frequencies = []
for i in range(n_intervals):
    lower_bound = bins[i]
    upper_bound = bins[i + 1]
    prob = norm.cdf(upper_bound, loc=mean, scale=std_dev) - norm.cdf(lower_bound, loc=mean, scale=std_dev)
    expected_frequencies.append(prob * len(data))


observed_frequencies = np.array(observed_frequencies)
expected_frequencies = np.array(expected_frequencies)

contingency_table = np.array([observed_frequencies, expected_frequencies])
contingency_table1 = np.array([data, [min_x+i*h for i in range(len(data))]])


chi2_statistic, p_value, dof, _ = chi2_contingency(contingency_table)
chi2_crit = chi_critical(len(data) -2 , alpha=alpha)

print("Статистика хи-квадрат наблюдаемое и критическое:", chi2_statistic, chi2_crit)


if chi2_crit < chi2_statistic:
    print("Отказываем в нулевой гипотезе о нормальности распределения.")
else:
    print("Нет оснований для отказа в нулевой гипотезе о нормальности распределения.")