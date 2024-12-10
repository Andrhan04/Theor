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

alpha = 0.1
x = [32.9, 55.5, 56.2, 43.1, 32.0, 47.3, 46.6, 33.8, 32.6]
y = [21.8, 39.4, 44.5, 51.9, 45.3, 8.7, 67.4, 33.1, 28.4]

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
    F_crit = Fisher.GetCrit(alpha/2,len(data_x),len(data_y))
    print(F)
    print(F_crit)
    if(F < F_crit):
        print("– нет оснований отвергнуть гипотезу")
    else:
        print("– гипотезу отвергают.")

main()