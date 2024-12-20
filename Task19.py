'''
Задание 19. 
Используя метод наименьших квадратов, найти параметры линейной, квадратичной и показательной зависимостей аппроксимирующей функции. 
Определить, какая из функций является лучшим приближением зависимости между х и у.

'''
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def mapping(values_x, a, b):     
    return a*values_x + b

def mapping_sq(values_x, a, b, c):     
    return a*(values_x**2) + b*(values_x) + c

def mapping_p(values_x, a):
    return a**values_x

def mapping_my(values_x, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11):     
    return (a0 + a1 * values_x + a2*(values_x**2) + a3*(values_x**3)+ a4*(values_x**4) + a5*(values_x**5)
            + a6*(values_x**6)+ a7*(values_x**7) + a8*(values_x**8)+ a9*(values_x**9)+ a10*(values_x**10)
            + a11*(values_x**11)
    )

x_data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0]
y_data = [1.1, 2.6, 2.7, 3.0, 4.1, 4.6, 4.7, 3.4, 4.8, 5.1, 5.7, 5.2, 5.6]
def main(xdata = x_data, ydata = y_data):
    plt.figure()
    plt.plot(xdata, ydata, color='b', label='Data')
    args, covar = curve_fit(mapping, xdata, ydata) 
    a=args[0]
    b=args[1]
    print(a,b)
    yint=[]
    for x in xdata:
        yint.append(mapping(x,a,b))
    so = r2_score(y_true=ydata,y_pred=yint)
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
    so = r2_score(y_true=ydata,y_pred=yint)
    print(so)
    plt.plot(xdata, yint, color='g', linestyle='dashed', label='Squeare')
    #-----------------------------------------------------------------------------------------
    args, covar = curve_fit(mapping_p, xdata, ydata) 
    a=args[0]
    print(a)
    yint=[]
    for x in xdata:
        yint.append(mapping_sq(x,a,b,c))
    so = r2_score(y_true=ydata,y_pred=yint)
    so = round(so,3)
    print(so)
    plt.plot(xdata, yint, color='black', linestyle='dashed', label='Squeare')
    plt.show()
    #------------------------------------------------------------------
    # args, covar = curve_fit(mapping_my,xdata,ydata)
    # yint=[]
    # for x in xdata:
    #     yint.append(mapping_my(x,args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],args[11]))
    # so = r2_score(y_true=ydata,y_pred=yint)
    print(so)

main()