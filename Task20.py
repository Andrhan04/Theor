import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

data = np.array([9192, 9161, 9162, 9163, 9128, 9114, 9113, 9126, 9127, 9115, 9122,
                9111, 9121, 9137, 9112, 9064, 9074, 9072, 9073, 9098, 9086, 9088,
                9099, 9096, 9097, 9125, 9036, 9034, 9033, 9028])

def main(data = data):

    # 1. Найти выборочные оценки математического ожидания, дисперсии и среднеквадратического отклонения
    mean_estimate = np.mean(data)
    variance_estimate = np.var(data, ddof=1)  # с поправкой на выборку
    std_dev_estimate = np.std(data, ddof=1)    # с поправкой на выборку

    print(f'Выборочное математическое ожидание: {mean_estimate:.2f}')
    print(f'Выборочная дисперсия: {variance_estimate:.2f}')
    print(f'Выборочное среднеквадратическое отклонение: {std_dev_estimate:.2f}')

    # 2. Составить группированный вариационный ряд
    bins = np.arange(100, 1200, 100)  # Определяем границы классов
    hist, edges = np.histogram(data, bins=bins)

    # Создаем DataFrame для вариационного ряда
    variational_series = pd.DataFrame({
        'Границы классов': [f"{edges[i]} - {edges[i+1]}" for i in range(len(edges)-1)],
        'Частоты': hist,
        'Относительные частоты': hist / len(data)
    })

    print("\nГруппированный вариационный ряд:")
    print(variational_series)

    # 3. Построить гистограмму и полигон относительных частот
    plt.figure(figsize=(12, 6))
    sns.histplot(data, bins=bins, kde=False, stat="density", color='c', label='Гистограмма', alpha=0.6)

    # Полигон относительных частот
    relative_freq = hist / len(data)  # Относительные частоты
    mid_points = edges[:-1] + np.diff(edges) / 2
    plt.plot(mid_points, relative_freq, marker='o', color='r', label='Полигон относительных частот')

    plt.title('Гистограмма и полигон относительных частот')
    plt.xlabel('Значения')
    plt.ylabel('Плотность вероятности')
    plt.legend()
    plt.grid()
    plt.show()

    # 4. Построить график теоретической плотности вероятностей
    x = np.linspace(100, 1100, 100)
    pdf = stats.norm.pdf(x, mean_estimate, std_dev_estimate)

    plt.figure(figsize=(12, 6))
    sns.histplot(data, bins=bins, stat="density", color='c', label='Гистограмма', alpha=0.6)
    plt.plot(x, pdf, color='m', label='Теоретическая плотность вероятности')

    plt.title('Гистограмма и теоретическая плотность вероятности')
    plt.xlabel('Значения')
    plt.ylabel('Плотность вероятности')
    plt.legend()
    plt.grid()
    plt.show()

    # 5. Составить эмпирическую функцию распределения
    ecdf = np.arange(1, len(data) + 1) / len(data)
    sorted_data = np.sort(data)

    plt.figure(figsize=(12, 6))
    plt.step(sorted_data, ecdf, label='Эмпирическая функция распределения', where='post')
    plt.xlabel('Значения')
    plt.ylabel('Эмпирическая частота')
    plt.title('Эмпирическая функция распределения')
    plt.grid()
    plt.legend()
    plt.show()

    # 6. Построить график теоретической функции распределения
    plt.figure(figsize=(12, 6))
    plt.step(sorted_data, ecdf, label='Эмпирическая функция распределения', where='post')
    plt.plot(x, stats.norm.cdf(x, mean_estimate, std_dev_estimate), color='m', label='Теоретическая функция распределения')

    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.title('Эмпирическая и теоретическая функции распределения')
    plt.grid()
    plt.legend()
    plt.show()

    # 7. Проверка гипотезы о виде распределения с помощью критерия χ²
    # Подсчет ожидаемых частот для критерия Хи-квадрат
    expected_freq = stats.norm.pdf(mid_points, mean_estimate, std_dev_estimate) * len(data)

    # Расчет критерия Хи-квадрат
    chi_square_stat = np.sum((hist - expected_freq) ** 2 / expected_freq)
    df = len(mid_points) - 1 - 2  # количество классов - 1 - количество оцененных параметров
    alpha = 0.1
    critical_value = stats.chi2.ppf(1 - alpha, df)

    print(f'Статистика Хи-квадрат: {chi_square_stat:.2f}, Критическое значение: {critical_value:.2f}')

    if chi_square_stat > critical_value:
        print("Отвергаем H0: распределение не нормальное")
    else:
        print("Не отвергаем H0: распределение может быть нормальным")

    # 8. Построение доверительных интервалов
    def confidence_interval(mean, std_dev, n, alpha):
        z = stats.norm.ppf(1 - alpha / 2)  # Z-критическое значение для нормального распределения
        lower_bound = mean - z * (std_dev / np.sqrt(n))
        upper_bound = mean + z * (std_dev / np.sqrt(n))
        return lower_bound, upper_bound

    n = len(data)
    alpha_levels = [0.1, 0.05, 0.01]
    for alpha in alpha_levels:
        lower, upper = confidence_interval(mean_estimate, std_dev_estimate, n, alpha)
        print(f'Доверительный интервал для α={alpha}: ({lower:.2f}, {upper:.2f})')