import statistics 
from math import sqrt

data = [30.7, 28.9, 37.9, 32.2, 32.1, 34.0, 30.9, 32.6, 30.0, 34.5, 34.5, 29.5, 31.0, 27.4, 30.2, 33.6, ]
#распределение стьюдента
def main(data = data):
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
    
main()
