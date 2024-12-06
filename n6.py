import statistics 
from math import sqrt

data = [14.4 ,15.5 ,14.8 ,15.7 ,14.1 ,14.7 ,14.6 ,14.4 ,14.2 ,16.6 ,14.0 ,14.1, 15.7 ,14.8 ,14.1 ,14.6]
#распределение стьюдента
print(len(data)-1)
n: int = len(data)
gamma = 0.95
X: float = statistics.mean(data)
S: float = statistics.variance(data, X)
t = 2.13 #по ПРИЛОЖЕНИЕ 2
print(f'{S:.5f}')

delta = t * S / sqrt(n)
print(f'{X:.5f}')
print(f'{delta:.5f}')
print(f'границы довер. инервала: {X-delta:.5f}; {X+delta:.5f}')
