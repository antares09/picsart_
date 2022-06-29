import random


def random_passwd(n):
    lst = []
    i = 0
    while (i < n):
        lst.append(chr(random.randint(33, 126)))
        i += 1
    str = ''.join(lst)
    return str


print(random_passwd(8))