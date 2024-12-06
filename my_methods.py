import scipy
import numpy as np
import statistics

data = scipy.stats.norm.cdf(np.linspace(0,1,101)) - 0.5


d = {}
n = 0
for i in data:
    d[n] = round(float(i), 4)
    n = round(n+0.01, 3)
    
    
def F(x):
    return d[x]




def my_mean(data_x, data_p):
    data = []
    for i in range(len(data_x)):
        data += data_p[i] * [data_x[i]]
    return statistics.mean(data)


def my_variance(data_x, data_p):
    data = []
    for i in range(len(data_x)):
        data += data_p[i] * [data_x[i]]
    return statistics.variance(data)