def get_median(data):
    data = sorted(data, reverse=False)
    if len(data) % 2 == 0:
        med = (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2
    else:
        med = data[len(data) // 2]

    return med


lst = [1, 2, 3, 5, 8, 10, 11, 12, 13, 7]
print(get_median(lst))