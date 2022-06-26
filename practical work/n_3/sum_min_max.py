def sum_of_min_max(data):
    min = data[0]
    max = data[0]
    for i in data:
        if max < i:
            max = i
        if min > i:
            min = i
    return min + max


lst = [3, 5, 17, 11, 12]
print(sum_of_min_max(lst))