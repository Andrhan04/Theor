from collections import Counter
from my_methods import chi_critical, chi_obvervable
import numpy as np
from scipy.stats import chi2_contingency, norm
from math import sqrt

data = [
    35.1, 46.7, 23.9, 50.5, 32.3, 32.5, 32.7, 21.5, 33.1, 34.0, 42.4, 53.6,
    34.8, 18.7, 25.7, 29.1, 18.4, 38.8, 23.6, 19.5, 22.7, 26.8, 54.1, 47.4,
    42.0, 24.0, 35.9, 58.1, 45.1, 5.8, 27.6, 25.4, 40.8, 41.5, 18.3, 36.5,
    30.3, 29.5, 30.0, 58.1, 43.2, 28.1, 17.4, 30.4, 45.9, 42.6, 33.7, 42.8,
    32.5, 21.4, 30.0, 45.8, 29.2, 42.9, 18.9, 26.2, 23.3, 42.8, 42.6, 35.8,
    33.5, 38.8, 38.9, 42.2, 32.0, 32.9, 29.2, 42.1, 28.3, 50.2, 46.5, 32.4,
    16.2, 36.8, 33.5, 31.6, 23.0, 46.6, 18.7, 30.4, 29.4, 21.8, 36.1, 34.2,
    39.5, 32.9, 33.5, 24.1, 6.0, 17.8, 21.1, 42.6, 30.4, 29.1, 52.3, 37.4,
    39.9, 39.1, 37.5, 41.6
]

'''
По данным выборки проверить с помощью критерия Пирсона
при уровне значимости α гипотезу:
а) о показательном;
б) равномерном;
в) нормальном законе распределения генеральной совокупности.
В ответе привести:
1) выбранную гипотезу о виде закона распределения;
2) вычисленное значение критерия;
3) критическое значение;
4) вывод о принятии или не принятии гипотезы
'''

def main(data = data, alpha = 0.025):
    a = [[]]
    q = [0] * 10
    data = sorted(data)
    counter = Counter(sorted(data))
    data_x = list(counter.keys())
    data_p = list(counter.values())
    r = max(data) - min(data)
    print(r)
    h = r/10
    print(h)
    intervals = [[min(data) + r/10*i, min(data) + r/10*(i+1)] for i in range(10)]
    intervals[-1][1] = intervals[-1][1] + 0.005
    print(intervals)
    for i in data:
        for j in range(len(intervals)):
            if intervals[j][0] <= i < intervals[j][1]:
                q[j] += 1
                break
    intervals[0] = [5.8, 21.49]
    intervals.pop(2)
    intervals.pop(1)
    q[0] = 13
    q.pop(2)
    q.pop(1)
    intervals[-1] = [47.64, 58.105]
    intervals.pop(-2)
    q[-1] = 7
    q.pop(-2)
    for i in range(len(q)):
        print(intervals[i], q[i])
    X = sum(list(map(lambda x,y: (x[0]+x[1])*y/2, intervals, q))) / sum(q)
    D = sum(list(map(lambda x,y: (x[0]+x[1])*(x[0]+x[1])*y/4, intervals, q))) / sum(q) - X*X
    sigma = sqrt(D)
    print(X, D, sigma)
    
    a = X - sqrt(3) * sigma
    b = X + sqrt(3) * sigma
    print(a, b)
    fx = 1/(b-a)
    
    n = [0] * 7
    
    n[0] = sum(q) * (intervals[0][1] - a) * fx
    
    for i in range(1, 6):
        n[i] = sum(q) * (intervals[i][1] - intervals[i][0]) * fx
        
    n[-1] = sum(q) * (b - intervals[-1][0]) *fx
    
    print(n)
    
    for i in range(len(q)):
        print(intervals[i], q[i])
    
    s1 = sum(list(map(lambda x, y: (x-y)*(x-y) / y, q, n)))
    chi2_crit = chi_critical(len(n) -2 , alpha=alpha)
    
    
    
    
    print(s1, chi2_crit)
if __name__ == '__main__':
    main()