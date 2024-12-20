# Задание 10. 
# Для заданного интервального выборочного ряда 
# (начальное значениеmin x, шаг h) 
# проверить гипотезу: закон распределения генеральной совокупности является равномерным при уровне значимости
# alpha = 0,05
from my_methods import chi_critical, chi_obvervable

p = [42, 42, 46, 42, 46, 40, 37, 50, 37, 34]


def main(data_p = p ,x_min = 1.8, h = 1.8 , alpha= 0.05):

    data_x = [round(x_min + h*i,1) for i in range(len(data_p))]
    k = len(data_p) - 2
    ch = chi_critical(k, alpha)
    chi_obs = chi_obvervable(data_p=data_p, data_x=data_x)[0]
    print(ch)
    if ch > chi_obs:
        print("гипотеза отвергнута ")
    else:
        print("нет оснований отвергать!")


main()