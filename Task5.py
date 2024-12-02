import statistics as st
from Function import Laplas

# Задание 5. По данным выборки, удовлетворяющей нормальному закону
# распределения со средним квадратическим отклонением S , вычислить:
# 1) выборочное среднее;
# 2) доверительный интервал для математического ожидания при доверительной вероятности γ.
def main(data, y, s):
    x = st.mean(data) 
    print(x)
    Gran = Laplas.GetParm(y/2)
    print("({:.3f};{:.3f})".format(x-Gran,x+Gran))