'''

Для заданного интервального выборочного ряда 
(начальное значение min x , шаг h)
проверить гипотезу: закон распределения генеральной совокупности является нормальным при уровне значимости
alpha = 0,05.


'''
from my_methods import F, my_mean, my_variance, chi_critical, chi_obvervable
import statistics
from math import sqrt, fabs

alpha = 0.05
x_min = 0
h = 0.2
a0 = x_min
a1 = x_min + h

data_p = [156, 101, 57, 32, 14, 9, 11, 1, 2, 1, 1]
data_x = [round(x_min + h*i,1) for i in range(len(data_p))]

k = len(data_p) - 2

ch = chi_critical(k, alpha)
chi_obs = chi_obvervable(data_p=data_p, data_x=data_x, alpha=alpha)
print(ch)

if ch > chi_obs:
    print("гипотеза отвергнута ")
else:
    print("нет оснований отвергать!")