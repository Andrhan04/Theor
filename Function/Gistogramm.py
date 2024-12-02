import matplotlib.pyplot as plt


# Строим базовую гистограммe


def main(data):
# Строим базовую гистограмму
    y,Hist,_ = plt.hist(data, bins=30, color='white', edgecolor='white')
# Добавляем метки и заголовок
    plt.xlabel('Значения')
    plt.ylabel('Колличество')
    plt.title('полигон частот')
    mid=0.5*(Hist[1:] + Hist[:-1])
# Выводим график
    plt.plot(mid,y)
    plt.show()