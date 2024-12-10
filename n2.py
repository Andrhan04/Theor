

# Задание 2. Каждому студенту в соответствии со своим номером варианта
# требуется:
# + 1. Составить статистическое распределение выборки, предварительно записав дискретный вариационный ряд.
# + 2. Составить ряд распределения относительных частот.
# + 3. Построить полигон частот.
# + 4. Составить эмпирическую функцию распределения.
# + 5. Построить график эмпирической функции распределения.
# 6. Найти основные числовые характеристики вариационного ряда:
#  выборочное среднее
#  выборочную дисперсию
#  выборочное среднее квадратическое отклонение
#  коэффициент вариации.
# 7. Пояснить смысл полученных результатов.



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data = [4, 3, 1, 4, 5, 3, 0, 2, 4, 3, 2, 3, 4, 3, 1, 
        2, 3, 4, 0, 2, 5, 3, 3, 3, 3, 2, 0, 6, 2, 3, 
        1, 5, 2, 4, 2, 4, 3, 1, 2, 3, 2, 2, 2, 3, 4, 
        1, 6, 2, 3, 3, 2, 0, 6, 2, 5, 0, 2, 4, 3, 4, 
        6, 0, 2, 5, 3, 3, 3, 5, 4, 3, 1, 4, 5, 4, 3, 
        2, 1, 2, 3, 2, 2, 0, 2, 5, 3, 3, 1, 6, 2, 4, 
        6, 0, 4, 3, 1, 4, 5, 2, 4, 2, 4, 3, 2, 3, 4, 
        5, 2, 0, 2, 4, 3, 2, 1, 6, 2, 3, 3, 2, 0, 6, 
        0, 2, 5, 3, 3, 3, 1, 2, 3, 2, 2, 5, 2, 3, 4, 
        5, 4, 2, 2, 4, 2, 4, 3, 4, 3, 1, 4, 5, 2, 5]


data = np.array(data)


value_counts = pd.Series(data).value_counts().sort_index()
discrete_variation_series = value_counts.reset_index()
discrete_variation_series.columns = ['Значение', 'Частота']

print("Дискретный вариационный ряд:")
print(discrete_variation_series)


total_count = len(data)
discrete_variation_series['Относительная частота'] = discrete_variation_series['Частота'] / total_count

print("\nРяд распределения относительных частот:")
print(discrete_variation_series[['Значение', 'Относительная частота']])


plt.figure(figsize=(12, 6))
plt.plot(discrete_variation_series['Значение'], discrete_variation_series['Частота'], marker='o', label='Частота', color='b')
plt.title('Полигон частот')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid()
plt.legend()
plt.show()

sorted_data = np.sort(data)
ecdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

plt.figure(figsize=(12, 6))
plt.step(sorted_data, ecdf, label='Эмпирическая функция распределения', where='post')
plt.title('Эмпирическая функция распределения')
plt.xlabel('Значения')
plt.ylabel('Эмпирическая частота')
plt.grid()
plt.legend()
plt.show()

mean_x = np.mean(data)  # выборочное среднее
variance_dv = np.var(data, ddof=1)  # выборочная дисперсия
std_dev_v = np.std(data, ddof=1)  # выборочное среднее квадратическое отклонение
coefficient_of_variation_v = std_dev_v / mean_x * 100  # коэффициент вариации в процентах

print(f'\nОсновные числовые характеристики:')
print(f'Выборочное среднее: {mean_x:.2f}')
print(f'Выборочная дисперсия: {variance_dv:.2f}')
print(f'Выборочное среднее квадратическое отклонение: {std_dev_v:.2f}')
print(f'Коэффициент вариации: {coefficient_of_variation_v:.2f}%')


# Смысл результатов: 
# Выборочное среднее показывает, что в среднем данные находятся на уровне ~73.50.
# Выборочная дисперсия и стандартное отклонение показывают разброс данных, где стандартное отклонение ~7.25,
# что говорит о том, что значения в выборке в среднем отклоняются от среднего на 7.25.
# Коэффициент вариации позволяет оценить относительную изменчивость данных; в данном случае это ~9.85%,
# что говорит о том, что разброс значений не является слишком большим относительно среднего, 
# и выборка достаточно однородна.