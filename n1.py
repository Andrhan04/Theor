import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Составить статистическое распределение выборки, предварительно записав дискретный вариационный ряд.
# + Составить интервальный ряд распределения относительных частот.
# + Построить гистограмму относительных частот.
# + Составить эмпирическую функцию распределения.
# + Построить график эмпирической функции распределения.
data = np.array([63.5, 69.8, 64.7, 70.8, 77.5, 82.1, 86.1, 83.3, 85.9, 69.8,
                 69.8, 70.8, 82.1, 86.1, 75.3])
def main(data=data):
    value_counts = pd.Series(data).value_counts().sort_index()
    discrete_variation_series = value_counts.reset_index()
    discrete_variation_series.columns = ['Значение', 'Частота']

    print("Дискретный вариационный ряд:")
    print(discrete_variation_series)

    bins = np.arange(60, 90, 5)  
    hist, edges = np.histogram(data, bins=bins)

    interval_distribution = pd.DataFrame({
        'Интервал': [f"{edges[i]} - {edges[i + 1]}" for i in range(len(edges) - 1)],
        'Частота': hist,
        'Относительная частота': hist / len(data)
    })

    print("\nИнтервальный ряд распределения относительных частот:")
    print(interval_distribution)

    plt.figure(figsize=(12, 6))
    sns.histplot(data, bins=bins, stat="probability", kde=False, color='c', label='Гистограмма относительных частот', alpha=0.6)

    plt.title('Гистограмма относительных частот')
    plt.xlabel('Значения')
    plt.ylabel('Относительная частота')
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
    
main()