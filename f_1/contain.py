def contain(data, val):
    ''' Checks if an item is in the list or not '''
    for i in data:
        if i == val:
            return True
    return False


lst = [4, 25, 1, 6, 9, 12, 36, 8]
print(contain(lst, 36))
