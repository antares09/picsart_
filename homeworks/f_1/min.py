def min(data):
    ''' Returns the smallest member of the data '''
    _min = data[0]
    for i in data:
        if i < _min:
            _min = i
    return _min


lst = [4, 25, 1, 6, 9, 12, 36, 8, 1, 2, 1, 3]
print(min(lst))