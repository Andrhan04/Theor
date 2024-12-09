from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def mapping(values_x, a, b):     
    return a*values_x + b

def mapping_sq(values_x, a, b, c):     
    return a*(values_x**2) + b*(values_x) + c

def mapping_p(values_x, a):
    return a**values_x

xdata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ydata = [0.1, 1.5, 2.8, 8.2, 20.2, 55.4, 127.5, 223, 497.6, 980]

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
print('----')
print(a)

yint=[]
for x in xdata:
    yint.append(mapping_p(x,a))

so = 0
for i in range(len(ydata)):
    if(ydata[i] !=0):
        so += abs(yint[i]-ydata[i])/ydata[i]
so = so / (len(ydata)) * 100
so = round(so,3)
print(so)
plt.plot(xdata, yint, color='black', linestyle='dashed', label='Squeare')

plt.show()
