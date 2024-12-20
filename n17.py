import numpy as np

"""
Два студента ответили на пять тестов. Результаты их тестирования таковы:
Тесты 1 2 3 4 5
1 студент 8 5 4 7 9
2 студент 4 6 4 8 5
На основе рангового коэффициента Спирмена найдите значимость различий в результатах тестирования студентов, рассматривая данные, как выборочные
наблюдения случайных величин. Сделать выводы
"""


student_1 = [8, 5, 4, 7, 9]
student_2 = [4, 6, 4, 8, 5]


def rank(data):
    sorted_data = sorted(data)
    ranks = np.zeros(len(data))
    for i, val in enumerate(data):
        ranks[i] = sorted_data.index(val) + 1  # +1 так как ранги начинаются с 1
        # Если есть дубликаты, присваиваем средний ранг
        num_occurrences = sorted_data.count(val)
        if num_occurrences > 1:
            ranks[i] = sum(range(sorted_data.index(val) + 1, sorted_data.index(val) + num_occurrences + 1)) / num_occurrences
    print(f'rank {data} = {ranks}')
    return ranks


def spearman_correlation(student_1, student_2):
    rank_1 = rank(student_1)
    rank_2 = rank(student_2)
    
   
    d = rank_1 - rank_2
    d_squared_sum = sum(d_i ** 2 for d_i in d)
    
    n = len(student_1)  
    r_s = 1 - (6 * d_squared_sum) / (n * (n**2 - 1))  # коэффициент рангов Спирмена

    return r_s

# Функция для вычисления значимости
def spearman_significance(r_s, n):
    # Этот пример использует приближенную нормализацию для малых выборок
    z = 0.5 * np.log((1 + r_s) / (1 - r_s))  # Вычисляем Z-статистику
    z_critical = 1.96  # Критическое значение Z для уровня значимости 0.05 для двустороннего теста
    p_value = 2 * (1 - (1 / (1 + np.exp(z))))  # Приблизительное p-значение
    return p_value

def main(student_1=student_1, student_2=student_2):
    r_s = spearman_correlation(student_1, student_2)
    n = len(student_1)
    p_value = spearman_significance(r_s, n)

    # Код для вывода результатов
    print(f"Коэффициент Спирмена (r_s): {r_s:.4f}")
    print(f"P-значение: {p_value:.4f}")

    # Вывод результатов
    if p_value < 0.05:
        print("Существуют значительные различия в результатах тестирования студентов.")
    else:
        print("Нет значительных различий в результатах тестирования студентов.")
        
main()