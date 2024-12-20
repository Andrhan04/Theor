import statistics as st
from Function import Laplas
from math import sqrt
# Задание 5. По данным выборки, удовлетворяющей нормальному закону
# распределения со средним квадратическим отклонением S , вычислить:
# 1) выборочное среднее;
# 2) доверительный интервал для математического ожидания при доверительной вероятности γ.
data = [-6.8, 5.2, 4.0, 5.8, -9.8, 5.8, 1.8, 13.3, -9.7, 2.3, -4.0, -1.7,
        -10.4, 13.4, 17.7, -6.7, -2.5, -5.1, 6.1, 1.1, 0.1, 8.1, 1.9, 7.7,
        6.9, 4.6, 0.7, 4.1, 2.6, -0.9, -1.3, 2.8, -3.7, 7.5, -6.3, 1.5,
        -3.5, -0.2, 0.1, 8.0, -0.7, -6.1, 5.3, 12.2, -0.4, 4.6, 8.4, 6.8,
        3.7, 4.0, -0.7, -1.2, -3.3, -10.9, 11.4, 3.4, -9.1, -1.4, 8.0,
        -1.2, 7.5, -2.6, 15.4, 8.0, 4.6, 3.2, 7.5, 1.5, 1.9, 15.2, 5.7,
        -17.0, -9.5, -4.9, 6.9, -5.9, -2.8, 5.4, -11.8, 9.0, -3.8, 3.5,
        -1.3, 11.6, 0.5, -3.0, 8.4, -7.9, -5.7, -2.7, 2.2, -4.8, 4.0, 2.4,
        -13.3, -2.0, -3.3, -1.0, -3.0, -1.9]
def main(data = data, y = 0.95, s = 6):
    x = st.mean(data) 
    print(x)
    Gran = Laplas.GetParm(y/2) * s / sqrt(len(data))
    print("({:.3f}; {:.3f})".format(x-Gran,x+Gran))

main()
