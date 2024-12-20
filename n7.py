'''
При 120 бросаниях игральной кости шестерка выпала 24 раза, пятерка 19
раз, четверка 22 раза, тройка 22 раза, двойка 17 раз, единица 16 раз. С помощью
критерия Пирсона проверить, согласуется ли этот результат с утверждением, что
кость правильная? Принять alpha = 0,05.
'''



import statistics
from scipy.stats import chi2_contingency, chisquare
import pandas as pd
from my_methods import chi_critical, chi_obvervable
import numpy as np

data = {
    'x' : [6, 5, 4, 3, 2 ,1],
    'p' : [24, 19, 22, 22, 17, 16]

}

observed_frequencies = np.array(data['p'])


N = 120  
expected_frequencies = np.array([N / 6] * 6)  


alpha: float = 0.5
df = pd.DataFrame(data)
#на нем закончили

#print(statistics.mean(data_x))
contingency_table = pd.crosstab(df['x'], df['p'])
print(contingency_table)

chi2, p = chisquare(observed_frequencies, expected_frequencies)

print(f"x: {chi2}, p-значение: {p}")

if p >= alpha: 
    print('гипотеза отвергнута')
    
else:
    print('нет оснований отвергать гипотезу')