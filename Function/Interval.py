import numpy as np

#  Число - вероятность
#  Составить интервальный ряд распределения относительных частот.

def main(data):
    data.sort()
    n = len(data)
    dataSet = {}
    for x in data:
        if x not in dataSet:
            dataSet[x] = 1/n
        else:
            dataSet[x] += 1/n
    data_uniqs = np.unique(data)
    for x in data_uniqs:
        print(x, dataSet[x])