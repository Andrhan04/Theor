import numpy as np
import math
import statistics as st


def main(data):
    data.sort()
    dataSet = {}
    n = len(data)
    data_uniqs = np.unique(data)
    for x in data:
        if x not in dataSet:
            dataSet[x] = 1
        else:
            dataSet[x] += 1
    ans = 0.0
    for x in data_uniqs:
        ans += x * dataSet[x]
    ans /= n
    # print(st.mean(data)) # стандартная функкция X
    print("xв =", ans)

    s = 0.0
    for x in data_uniqs:
        s += (x - ans) * (x - ans) * dataSet[x]
    s/=n
    # print(st.variance(data)) # стандартная функкция D
    print("s =", s)
    print("o =",math.sqrt(s))
    print("V =", math.sqrt(s)/ans * 100)