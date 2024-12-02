import matplotlib.pyplot as plt
import numpy as np

# Построить график эмпирической функции распределения

def main(data):
    bin_dt, bin_gr = np.histogram(data, bins=len(data))
    Y = bin_dt.cumsum()
    for i in range(len(Y)):
        plt.plot([bin_gr[i], bin_gr[i+1]],[Y[i]/len(data), Y[i]/len(data)],color='green')
    plt.title('эмпирическая функция распределения ')
    plt.show()