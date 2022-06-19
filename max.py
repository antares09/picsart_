def max(data):
    ''' Returns the biggest member of the data '''
    _max = data[0]
    for i in data:
        if i > _max:
            _max = i
    return _max


lst = [4, 25, 1, 6, 9, 12, 36, 8, 1, 2, 1, 3]
print(max(lst))