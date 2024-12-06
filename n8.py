'''

Для заданного интервального выборочного ряда 
(начальное значение min x , шаг h)
проверить гипотезу: закон распределения генеральной совокупности является нормальным при уровне значимости
alpha = 0,05.


'''
from my_methods import F, my_mean, my_variance
import statistics
from math import sqrt

alpha = 0.1
x_min = 2.4
h = 1.4
a0 = x_min
a1 = x_min + h

data_p = [3, 10, 31, 57, 88, 75, 47, 30, 9, 2]

data_x = [round(x_min + h*i,1) for i in range(len(data_p))]
my_mean(data_x=data_x, data_p=data_p)
data = {'x' : data_x, 'p' : data_p}
X = my_mean(data_x=data_x, data_p=data_p)
S = my_variance(data_x=data_x, data_p=data_p)
for i in range(len(data_x)-1):
    print(F((data_x[i+1]-X)/sqrt(S)) - F( (data_x[i] - X) / sqrt(S) ))

print(data_p)
print(data_x)