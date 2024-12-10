from collections import Counter
from my_methods import chi_critical, chi_obvervable

data = [
    35.1, 46.7, 23.9, 50.5, 32.3, 32.5, 32.7, 21.5, 33.1, 34.0, 42.4, 53.6,
    34.8, 18.7, 25.7, 29.1, 18.4, 38.8, 23.6, 19.5, 22.7, 26.8, 54.1, 47.4,
    42.0, 24.0, 35.9, 58.1, 45.1, 5.8, 27.6, 25.4, 40.8, 41.5, 18.3, 36.5,
    30.3, 29.5, 30.0, 58.1, 43.2, 28.1, 17.4, 30.4, 45.9, 42.6, 33.7, 42.8,
    32.5, 21.4, 30.0, 45.8, 29.2, 42.9, 18.9, 26.2, 23.3, 42.8, 42.6, 35.8,
    33.5, 38.8, 38.9, 42.2, 32.0, 32.9, 29.2, 42.1, 28.3, 50.2, 46.5, 32.4,
    16.2, 36.8, 33.5, 31.6, 23.0, 46.6, 18.7, 30.4, 29.4, 21.8, 36.1, 34.2,
    39.5, 32.9, 33.5, 24.1, 6.0, 17.8, 21.1, 42.6, 30.4, 29.1, 52.3, 37.4,
    39.9, 39.1, 37.5, 41.6
]



def main(data = data, alpha = 0.025):
    counter = Counter(sorted(data))
    data_x = list(counter.keys())
    data_p = list(counter.values())

    n = len(data)
    chi_obver = chi_obvervable(data_p, data_x)[0]
    
    k_exp = n - 2
    k_norm = n - 3
    k_even = n - 3 
    
    chi_crit_exp = chi_critical(k_exp, alpha)
    chi_crit_norm = chi_critical(k_norm, alpha)
    chi_crit_even = chi_critical(k_even, alpha)
    

    
    
    print(f"показательная гипотеза: хи-наблюдаемое: {chi_obver:.3f} хи-критическое: {chi_crit_exp:.3f}")
    if chi_crit_exp < chi_obver:
        print("гипотеза отвергнута ")
    else:
        print("нет оснований отвергать!")
    print(f"нормальная гипотеза: хи-наблюдаемое: {chi_obver:.3f} хи-критическое: {chi_crit_norm:.3f}")
    if chi_crit_norm < chi_obver:
        print("гипотеза отвергнута ")
    else:
        print("нет оснований отвергать!")
    print(f"равномерная гипотеза: хи-наблюдаемое: {chi_obver:.3f} хи-критическое: {chi_crit_even:.3f}")
    if chi_crit_even < chi_obver:
        print("гипотеза отвергнута ")
    else:
        print("нет оснований отвергать!")
    
    
    
    
    
if __name__ == '__main__':
    main()