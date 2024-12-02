import statistics as st

def main(data, alpha):
    stat, p = st.normaltest(data)  # Критерий согласия Пирсона
    print('Statistics=%.3f (отличие от табличного значения),\n p-value=%.3f (уровень значимости выборки)' % (stat, p))
    if p > alpha:
        print('Принять гипотезу о нормальности')
    else:
        print('Отклонить гипотезу о нормальности')
