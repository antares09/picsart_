def is_sublist(large, small):
    sub = []
    count = len(small)
    lst = [None] * len(small)
    c_large = []
    for i in large:
        c_large.append(i)
    if small == [] or small == large:
        return True
    for j in range(len(large) - len(small)):
        for i in range(len(small)):
            lst[i] = c_large[i]
        if lst == small:
            return True
        if len(c_large) > len(small):
            del c_large[0]
    return False


lst1 = [1, 2, 3, 4, 5, 6, 7]
lst2 = []
lst3 = [2, 3]
lst4 = [1, 2, 3, 4, 5, 7]
lst5 = [1, 2, 3, 4, 5, 6, 7]
print(is_sublist(lst1, lst2))
print(is_sublist(lst1, lst3))
print(is_sublist(lst1, lst4))
print(is_sublist(lst1, lst5))
