'''
Задание 13. По данным двух выборок нормального закона распределения
проверить гипотезу о равенстве генеральных средних (при конкурирующей гипотезе об их неравенстве) при уровне значимости α = 0,1.
В ответе привести:
    1) выборочное среднее для первой выборки;
    2) выборочное среднее для второй выборки;
    3) вычисленное значение критерия;
    4) табличное значение;
    5) вывод о принятии или не принятии гипотезы.
'''
import statistics as st
from math import sqrt
from Function import Laplas 

x = [46.6, -8.2, 85.1, 12.9, 100.5, 34.6, 58.7, 72.6, 106.4, 91.8, 80.6, 149.4]
y = [68.7, 101.2, 44.2, 55.4, 61.7, 56.0, 45.9, 31.8, 56.1, 68.1, 90.7, 82.9]

def main(data_x = x, data_y = y, alpha = 0.1):
    X = st.mean(data_x)
    Y = st.mean(data_y)
    D_x = st.variance(data_x)
    D_y = st.variance(data_y)
    n_x = len(data_x)
    n_y = len(data_y)
    Z = (X - Y) / sqrt(D_x/n_x + D_y/n_y)
    print(Z)
    Z_crit = Laplas.GetParm((1-alpha)/2)
    print(Z_crit)
    if abs(Z) < Z_crit:
         print("– нет оснований отвергнуть гипотезу")
    else:
        print("– гипотезу отвергают.")

main()