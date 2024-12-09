'''
Задание 19. 
Используя метод наименьших квадратов, найти параметры линейной, квадратичной и показательной зависимостей аппроксимирующей функции. 
Определить, какая из функций является лучшим приближением зависимости между х и у.

'''
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def mapping(values_x, a, b):     
    return a*values_x + b

def mapping_sq(values_x, a, b, c):     
    return a*(values_x**2) + b*(values_x) + c

def mapping_p(values_x, a):
    return a**values_x

xdata = [-2, -1, 0, 1, 4, 5, 6, 7, 8, 10]
ydata = [-8, -5, -3, 1, 10, 15, 16, 20, 22, 26]

plt.figure()
plt.plot(xdata, ydata, color='b', label='Data')

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
plt.plot(xdata, yint, color='r', linestyle='dashed', label='Linear')
#-----------------------------------------------------------------------------
args, covar = curve_fit(mapping_sq, xdata, ydata) 
a=args[0]
b=args[1]
c = args[2]
print(a,b,c)

yint=[]
for x in xdata:
    yint.append(mapping_sq(x,a,b,c))

so = 0
for i in range(len(ydata)):
    if(ydata[i] !=0):
        so += abs(yint[i]-ydata[i])/ydata[i]
so = so / (len(ydata)) * 100
so = round(so,3)
print(so)
plt.plot(xdata, yint, color='g', linestyle='dashed', label='Squeare')
#-----------------------------------------------------------------------------------------
args, covar = curve_fit(mapping_p, xdata, ydata) 
a=args[0]
print(a)

yint=[]
for x in xdata:
    yint.append(mapping_sq(x,a,b,c))

so = 0
for i in range(len(ydata)):
    if(ydata[i] !=0):
        so += abs(yint[i]-ydata[i])/ydata[i]
so = so / (len(ydata)) * 100
so = round(so,3)
print(so)
plt.plot(xdata, yint, color='black', linestyle='dashed', label='Squeare')

plt.show()