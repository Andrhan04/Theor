'''
При 120 бросаниях игральной кости шестерка выпала 24 раза, пятерка 19
раз, четверка 22 раза, тройка 22 раза, двойка 17 раз, единица 16 раз. С помощью
критерия Пирсона проверить, согласуется ли этот результат с утверждением, что
кость правильная? Принять alpha = 0,05.
'''
import statistics
from scipy.stats import chi2_contingency
import pandas as pd

data = {
    'x' : [6, 5, 4, 3, 2 ,1],
    'p' : [24, 19, 22, 22, 17, 16]

}
alpha: float = 0.5
df = pd.DataFrame(data)


#print(statistics.mean(data_x))
contingency_table = pd.crosstab(df['x'], df['p'])
print(contingency_table)

chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"x: {chi2}, p-значение: {p}")

if p >= alpha: 
    print('гипотеза отвергнута')
    
else:
    print('нет оснований отвергать гипотезу')