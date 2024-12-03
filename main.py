import Task1 as T1
import Task2 as T2
import Task3 as T3
import Task3 as T4


print("Number 1")
T1.main()

print("Number 2")
T2.main()

T3.main()


data = [36.9, 31.1, 18.4, 40.7, 29.5, 44.7, 48.7, 26.5, 19.4, 40.5, 33.6,
        34.1, 44.6, 29.5, 43.5, 43.5, 24.8, 38.0,]
y = 0.99
print(len(data))
T4.main(data,y)


from Function import Help
import Task10
data_p = [42, 42, 46, 42, 46, 40, 37, 50, 37, 34]
data_x = []
for h in range(len(data_p)):
    data_x.append(round(1.8 + 1.8*h,3))
Task10.main( Help.GetData(data_x,data_p),alpha = 0.1)

import Task12 as T12
alpha = 0.1
x = [32.9, 55.5, 56.2, 43.1, 32.0, 47.3, 46.6, 33.8, 32.6]
y = [21.8, 39.4, 44.5, 51.9, 45.3, 8.7, 67.4, 33.1, 28.4]

T12.main(x,y,alpha)

import Task13 as T13
alpha = 0.1
x = [46.6, -8.2, 85.1, 12.9, 100.5, 34.6, 58.7, 72.6, 106.4, 91.8, 80.6, 149.4]
y = [68.7, 101.2, 44.2, 55.4, 61.7, 56.0, 45.9, 31.8, 56.1, 68.1, 90.7, 82.9]

T13.main(x,y,alpha)