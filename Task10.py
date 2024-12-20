# Задание 10. 
# Для заданного интервального выборочного ряда 
# (начальное значениеmin x, шаг h) 
# проверить гипотезу: закон распределения генеральной совокупности является равномерным при уровне значимости
# alpha = 0,05

from Function.my_methods import chi_critical
from scipy.stats import chi2_contingency, norm
import numpy as np

data_p = [42, 42, 46, 42, 46, 40, 37, 50, 37, 34]
def main(data = data_p ,min_x = 1.8, h = 1.8 , alpha= 0.05):

    data_x = [round(min_x + h*i,1) for i in range(len(data_p))]
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

    chi2_statistic, p_value, dof, _ = chi2_contingency(contingency_table)
    chi2_crit = chi_critical(len(data) -2 , alpha=alpha)

    print("Статистика хи-квадрат наблюдаемое и критическое:", chi2_statistic, chi2_crit)


    if chi2_crit < chi2_statistic:
        print("Отказываем в нулевой гипотезе о равномерности распределения.")
    else:
        print("Нет оснований для отказа в нулевой гипотезе о равномерности распределения.")


main()

