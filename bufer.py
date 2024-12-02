from Function import Help
import Task10
data_p = [42, 42, 46, 42, 46, 40, 37, 50, 37, 34]
data_x = []
alpha = 0.10 
for h in range(len(data_p)):
    data_x.append(round(1.8 + 1.8*h,3))
Task10.main(Help.GetData(data_x,data_p),alpha)
