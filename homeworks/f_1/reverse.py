def reverse(data):
    ''' Rotates data in reverse order '''
    for i in range(len(data) // 2):
        data[i], data[len(data) - 1 - i] = data[len(data) - 1 - i], data[i]
        #tmp = data[i]
        #data[i] = data[len(data) - 1 - i]
        #data[len(data) - 1 - i] = tmp'''


lst = [4, 25, 1, 6, 9, 12, 36, 8, 1, 2, 1, 3]
reverse(lst)
print(lst)