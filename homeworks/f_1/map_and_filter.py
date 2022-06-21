def ft_map(data, func):
    res = func(data)
    return res


def triple(data):
    res = [None] * len(data)
    len1 = 0
    for i in data:
        res[len1] = i * 3
        len1 += 1
    return res


def sum(num1, num2, num3):
    return num1 + num2 + num3


def map3(func, data1, data2, data3):
    res = [None] * len(data1)
    for i in range(len(data1)):
        res[i] = func(data1[i], data2[i], data3[i])
    return res

  
lst = [4, 25, 1, 6, 9, 12, 36, 8]
print(ft_map(lst, triple))
lst1 = [1, 1, 1, 1, 1]
lst2 = [2, 2, 2, 2, 2]
lst3 = [1, 2, 3, 4, 5]
print(map3(sum, lst1, lst2, lst3))