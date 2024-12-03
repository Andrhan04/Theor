'''
Задание 12. По двум выборкам нормальных законов распределения 
проверить гипотезу о равенстве дисперсий (при конкурирующей гипотезе об их неравенстве) при уровне значимости 0,1.
Определить:
    1) дисперсию первой выборки;
    2) дисперсию второй выборки;
    3) вычисленное значение критерия;
    4) теоретическое значение критерия;
    5) вывод о принятии или не принятии гипотезы
'''
import statistics as st
from Function import Fisher

def main(data_x, data_y, alpha):
    print(len(data_x),len(data_y))
    print(D_x:=st.variance(data_x))
    print(D_y:=st.variance(data_y))
    D_x *= len(data_x)/(len(data_x)-1)
    D_y *= len(data_y)/(len(data_y)-1)
    if(D_x>D_y):
        F = D_x/D_y
    else:
        F = D_y/D_x
    F_crit = Fisher.GetCrit(alpha/2,len(data_x),len(data_y))
    print(F)
    print(F_crit)
    if(F < F_crit):
        print("– нет оснований отвергнуть гипотезу")
    else:
        print("– гипотезу отвергают.")