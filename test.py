import numpy as np
from scipy.stats import chi2

def chi2_contingency_manual(observed):
    # Преобразуем входные данные в numpy-массив
    observed = np.array(observed)
    
    # Сумма по строкам и столбцам
    row_sums = observed.sum(axis=1)
    col_sums = observed.sum(axis=0)
    total = observed.sum()
    
    # Вычисление ожидаемых значений
    expected = np.outer(row_sums, col_sums) / total
    
    # Вычисление статистики χ²
    chi2_stat = ((observed - expected) ** 2 / expected).sum()
    
    # Число степеней свободы
    degrees_of_freedom = (observed.shape[0] - 1) * (observed.shape[1] - 1)
    
    # Вычисление p-значения
    p_value = chi2.cdf(chi2_stat, degrees_of_freedom)
    
    return chi2_stat, p_value, degrees_of_freedom

# Пример использования
observed_data = [[6, 5, 4, 3, 2 ,1], [24, 19, 22, 22, 17, 16]]

chi2_statistic, p_value, dof = chi2_contingency_manual(observed_data)
print(f"χ² статистика: {chi2_statistic:.4f}")
print(f"p-значение: {p_value:.4f}")
print(f"Степени свободы: {dof}")