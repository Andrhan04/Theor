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
def main(data_x,data_y, alpha):
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