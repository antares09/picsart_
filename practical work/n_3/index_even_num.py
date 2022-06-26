def index_even(data):
    lst = []
    for i in range(len(data)):
        if data[i] % 2 == 0:
            lst.append(i)
    return lst


lst = [2, 15, 14, 28, 96, 25]
print(*(index_even(lst)), sep=", ")
