import statistics as st
import scipy.stats as sps

# stat - показывает различия между фактическими данными в выборке и теоретическими результатами

# P-value – это минимальный уровень значимости, на котором нулевая гипотеза может быть отвергнута. 
# Соответственно, 
#   если p−value меньше нашего фиксированного уровня значимости, на котором мы проверяем гипотезу, 
#          то нулевую гипотезу следует отвергнуть,
#    если более – то отвергать нулевую гипотезу оснований нет.

def Normal(data, alpha):
    sample = sps.norm.rvs(size=1000)
    stat, p = st.normaltest(data)  # Критерий согласия Пирсона
    s,p_val = st.chisquare(data,sample)
    print(s,p_val)
    print('Statistics=%.3f (отличие от табличного значения),\n p-value=%.3f (уровень значимости выборки)' % (stat, p))
    if p > alpha:
        print('Принять гипотезу о нормальности')
    else:
        print('Отклонить гипотезу о нормальности')

def uniform(data, alpha):
    stat, p_val = st.chisquare(data)

    print(stat,p_val)    
    if p_val > alpha:
        print('Принять гипотезу')
    else:
        print('Отклонить гипотезу')
