'''
Задание 18. 
Используя метод наименьших квадратов, найти уравнение прямой по экспериментальным данным, и построить эту прямую. 
Сравнить полученный результат с результатом расчета в пакете «Анализ данных».
'''
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def mapping(values_x, a, b):     
    return a*values_x + b

xdata = [-2, -1, 0, 1, 4, 5, 6, 7, 8, 10]
ydata = [-8, -5, -3, 1, 10, 15, 16, 20, 22, 26]

args, covar = curve_fit(mapping, xdata, ydata) 
a=args[0]
b=args[1]
print(a,b)

yint=[]
for x in xdata:
    yint.append(mapping(x,a,b))

so = 0
for i in range(len(ydata)):
    if(ydata[i] !=0):
        so += abs(yint[i]-ydata[i])/ydata[i]
so = so / (len(ydata)) * 100
so = round(so,3)
print(so)

plt.figure()
plt.plot(xdata, ydata, color='b', label='Data')
plt.plot(xdata, yint, color='r', linestyle='dashed', label='Aproxim')
plt.title("Выжившие частицы")
plt.legend()
plt.show()