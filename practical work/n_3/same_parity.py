def same_parity(n, *args):
    lst = []
    lst1 = list(args)
    for i in range(len(args)):
        if int(lst1[i]) % n == 0:
            lst.append(args[i])
    return lst


lst = same_parity(4, 7, 4, 16, 54, 12, 3, 73, 65)
print(lst)