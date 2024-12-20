import statistics as st
from Function import Laplas

# Задание 4. По данным выборки, удовлетворяющей нормальному закону
# распределения, вычислить:
# 1) выборочное среднее;
# 2) исправленное выборочное среднее квадратическое отклонение;
# 3) доверительный интервал для математического ожидания при доверительной вероятности γ;
# 4) доверительный интервал для среднего квадратического отклонения для того же значения γ.

data = [36.9, 31.1, 18.4, 40.7, 29.5, 44.7, 48.7, 26.5, 19.4, 40.5, 33.6,
        34.1, 44.6, 29.5, 43.5, 43.5, 24.8, 38.0,]

def main(data = data, y=0.99):
    # стандартная функция для среднего
    print(max(data)-min(data))
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

main()
