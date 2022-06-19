def remove_all(data, val):
    '''Deletes all members in  data equal to value'''
    for i in data:
        if i == val:
            data.remove(val)


lst = [4, 25, 1, 6, 9, 12, 36, 8, 1, 2, 1]
remove_all(lst, 1)
print(lst)
