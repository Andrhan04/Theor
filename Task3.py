from Function import Distribution
from Function import Interval
from Function import Gistogramm
from Function import FuncDistribution
from Function import GrafFuncDistr
from Task2 import MainCheracter

# Задание 3. По данным выборки
# (n 100)
# требуется:
# 1. Составить статистическое распределение выборки, предварительно записав дискретный вариационный ряд.
# 2. Составить интервальный ряд распределения относительных частот.
# 3. Построить гистограмму относительных частот.
# 4. Составить эмпирическую функцию распределения.
# 5. Построить график эмпирической функции распределения.
# 6. Найти основные числовые характеристики вариационного ряда:
#  выборочное среднее
#  выборочную дисперсию
#  выборочное среднее квадратическое отклонение
#  коэффициент вариации
# 7. Пояснить смысл полученных результатов.

def main():
    data = [32.4, 33.5, 29.1, 32.7, 30.6, 31.1, 30.6, 30.2, 30.9, 32.1, 32.5, 33.8, 33.5, 32.2,
35.1, 31.5, 33.5, 28.7, 32.6, 30.6, 30.5, 27.9, 33.0, 30.8, 31.5, 28.8, 30.9, 33.4,
31.4, 27.4, 25.5, 29.5, 30.4, 32.5, 32.4, 36.5, 32.3, 30.8, 31.7, 31.1, 28.1, 27.7,
28.5, 31.3, 31.6, 35.1, 29.8, 33.0, 28.7, 28.6, 32.1, 29.6, 29.7, 32.3, 30.2, 33.5,
32.5, 30.2, 31.3, 34.0, 32.2, 32.2, 32.5, 28.2, 28.8, 30.5, 32.5, 32.6, 30.0, 36.1,
31.0, 28.1, 29.2, 32.3, 31.6, 32.2, 26.8, 33.1, 29.1, 33.9, 30.7, 28.9, 37.9, 32.2,
32.1, 34.0, 30.9, 32.6, 30.0, 34.5, 34.5, 29.5, 31.0, 27.4, 30.2, 33.6, 33.5, 29.0,
32.5, 30.6]
    print("p1")
    Distribution.main(data)
    print("p2")
    Interval.main(data)
    print("p3")
    Gistogramm.main(data)
    print("p4")
    FuncDistribution.main(data)
    print("p5")
    GrafFuncDistr.main(data)
    print("p6")
    MainCheracter.main(data)

main()
