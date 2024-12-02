from Function import Distribution
from Function import Interval
from Function import Gistogramm
from Function import FuncDistribution
from Function import GrafFuncDistr

# Задание 1. По данным выборки требуется:
# + Составить статистическое распределение выборки, предварительно записав дискретный вариационный ряд.
# + Составить ряд распределения относительных частот.
# + Построить полигон частот.
# + Составить эмпирическую функцию распределения.
# + Построить график эмпирической функции распределения.
# 15. Данные по группе предприятий о валовой продукции (млн руб.):
# 3; 5; 10; 6; 6; 4; 7; 7; 8; 8; 3; 5; 10; 6; 6.

def main():
    data = [3, 5, 10, 6, 6, 4, 7, 7, 8, 8, 3, 5, 10, 6, 6]
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