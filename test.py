import numpy as np
from scipy.stats import chi2

# Задаем уровни значимости (например, 0.10, 0.05, 0.01)
alpha_levels = [0.10, 0.05, 0.01]

# Задаем максимальное количество степеней свободы
max_df = 100

# Создаем словарь для хранения критических точек
critical_values = {}

# Вычисляем критические точки
for df in range(1, max_df + 1):
    critical_values[df] = {alpha: chi2.ppf(1 - alpha, df) for alpha in alpha_levels}

# Выводим критические значения для первых пятнадцати степеней свободы
for df, values in critical_values.items():
    print(f"Степени свободы: {df}, Критические значения: {values}")
    
    
print(critical_values[5][0.01])