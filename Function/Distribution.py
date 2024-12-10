import numpy as np

# число - колличество раз встреченно
# Составить статистическое распределение выборки, предварительно записав дискретный вариационный ряд. 

def main(data):
    data.sort()
    dataSet = {}
    for x in data:
        if x not in dataSet:
            dataSet[x] = 1
        else:
            dataSet[x] += 1
    data_uniqs = np.unique(data)
    for x in data_uniqs:
        print(x, dataSet[x])