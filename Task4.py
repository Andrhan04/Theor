import statistics as st
from Function import Laplas

# Задание 4. По данным выборки, удовлетворяющей нормальному закону
# распределения, вычислить:
# 1) выборочное среднее;
# 2) исправленное выборочное среднее квадратическое отклонение;
# 3) доверительный интервал для математического ожидания при доверительной вероятности γ;
# 4) доверительный интервал для среднего квадратического отклонения для того же значения γ.
def main(data, y):
    # стандартная функция для среднего
    x = st.mean(data) 
    print("Среднее = {:.3f}".format(x))
    # стандартная функция для дисперсии
    D = st.variance(data,x)
    print("Дисперсия = {:.3f}".format(D))
    D *= len(data)/(len(data)-1)
    print("Дисперсия исправленная = {:.3f}".format(D))
    Gran = Laplas.GetParm(y/2)
    print("({:.3f};{:.3f})".format(x-Gran,x+Gran))
    
    q = 0.66 # В табличке значений функции q = q(y,n) 

    print("({:.3f};{:.3f})".format(x*(1-q),x*(1+q)))
