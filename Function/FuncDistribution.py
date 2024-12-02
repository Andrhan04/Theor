import numpy as np

#Составить эмпирическую функцию распределения.

def main(data):
    data.sort()
    n = len(data)
    i = 1
    dataSet = {}
    for x in data:    
        dataSet[x] = i/n
        i+=1
    data_uniqs = np.unique(data)
    print(" x < {:3.2f} p = {:d}".format(data[0],0))
    for x in data_uniqs:
        print(" x > {:3.2f} p =  {:1.2f}".format(x,dataSet[x]))