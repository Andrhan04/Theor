from Function import Distribution
from Function import Interval
from Function import Gistogramm
from Function import FuncDistribution
from Function import GrafFuncDistr
from Function import MainCheracter

# Задание 2. Каждому студенту в соответствии со своим номером варианта
# требуется:
# + 1. Составить статистическое распределение выборки, предварительно записав дискретный вариационный ряд.
# + 2. Составить ряд распределения относительных частот.
# + 3. Построить полигон частот.
# + 4. Составить эмпирическую функцию распределения.
# + 5. Построить график эмпирической функции распределения.
# 6. Найти основные числовые характеристики вариационного ряда:
#  выборочное среднее
#  выборочную дисперсию
#  выборочное среднее квадратическое отклонение
#  коэффициент вариации.
# 7. Пояснить смысл полученных результатов.

def main():
    data = [3, 3, 3, 2, 0, 6, 1, 6, 2, 0, 2, 4, 3, 2, 0, 3, 5, 1, 2, 3, 2, 2, 5, 6, 2, 
            0, 2, 5, 3, 3, 4, 4, 3, 1, 4, 5, 2, 3, 4, 2, 4, 2, 4, 3, 6, 3, 4, 3, 1, 3, 
            3, 2, 0, 6, 3, 4, 3, 1, 2, 3, 4, 1, 0, 2, 4, 3, 2, 4, 3, 1, 4, 5, 1, 6, 2, 
            0, 2, 5, 3, 3, 0, 5, 3, 3, 2, 0, 6, 2, 3, 4, 4, 3, 1, 4, 5, 1, 2, 3, 2, 2, 
            0, 2, 5, 3, 3, 0, 2, 4, 2, 4, 3, 2, 6, 0, 2, 4, 3, 2, 3, 2, 0, 2, 5, 3, 3, 
            4, 3, 1, 4, 5, 2, 4, 2, 4, 3, 3, 3, 2, 0, 6, 2, 4, 0, 2, 4, 3, 2, 4, 3, 2, 
            5, 0, 2, 4, 3, 2, 3, 2, 1, 2, 3, 2, 2, 6, 5]
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