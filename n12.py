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
from my_methods import GetCrit

alpha = 0.1
x = [37.5, 39.9, 43.5, 37.8, 43.1, 35.2, 38.7, 32.2, 45.1, 35.7, 14.2, 38.2]
y = [32.7, 28.2, 24.7, 40.6, 26.8, 35.1, 44.3, 22.1, 25.7, 48.6, 41.3, 39.0]

def main(data_x = x, data_y = y, alpha = 0.1):
    print(len(data_x),len(data_y))
    print(D_x:=st.variance(data_x))
    print(D_y:=st.variance(data_y))
    D_x *= len(data_x)/(len(data_x)-1)
    D_y *= len(data_y)/(len(data_y)-1)
    if(D_x>D_y):
        F = D_x/D_y
    else:
        F = D_y/D_x
    F_crit = GetCrit(alpha/2,len(data_x),len(data_y))
    print(F)
    print(F_crit)
    if(F < F_crit):
        print("нет оснований отвергнуть гипотезу")
    else:
        print("гипотезу отвергают.")

main()