import random


def random_passwd(n):
    i = 0
    lst = []
    
    while (i < n):
        lst.append(chr(random.randint(33, 126)))
        i += 1
    str = ''.join(lst)
    return str


print(random_passwd(8))