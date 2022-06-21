def pop(data, index=None):
    ''' If no argument is passed, the last member is deleted, 
    otherwise the member in index i is deleted '''
    if index == None:
        data.remove(data[len(data) - 1])  #del data[len(data)-1]
    elif index < 0 or index >= len(data):
        raise ValueError
    else:
        data.remove(data[index])
    return data


lst = [4, 25, 1, 6, 9, 12, 36, 8]
print(pop(lst, 3))
print(pop(lst))
#print(pop(lst, 36))