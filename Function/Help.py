

def GetData(data_x,data_p):
    res = []
    for i in range(len(data_x)):
        res += [data_x[i]] * data_p[i]
    return res
        