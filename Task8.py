'''
Для заданного интервального выборочного ряда 
(начальное значение min x , шаг h)
проверить гипотезу: закон распределения генеральной совокупности является нормальным при уровне значимости
alpha = 0,05.
'''
from Function.my_methods import  chi_critical, chi_obvervable


p = [5, 7, 21, 66, 84, 90, 70, 20, 5, 3]
def main(data_p = p ,x_min = 10.1, h = 2.0, alpha= 0.1):

    data_x = [round(x_min + h*i,1) for i in range(len(data_p))]
    k = len(data_p) - 3
    ch = chi_critical(k, alpha)
    chi_obs = chi_obvervable(data_p=data_p, data_x=data_x, alpha=alpha)
    print(ch)
    if ch > chi_obs:
        print("гипотеза отвергнута ")
    else:
        print("нет оснований отвергать!")

main()