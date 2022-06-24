def zip(data1, data2):
    data = []
    for i in range(len(data1)):
        data.append(data1[i])
        data.append(data2[i])
    return data


lst1 = [1, 1, 1, 1, 1, 1]
lst2 = [2, 2, 2, 2, 2, 2]
print(zip(lst1, lst2))
