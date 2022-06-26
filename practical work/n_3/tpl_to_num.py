import copy


def int_len(n):
    count = 0
    num = n
    while num > 0:
        count += 1
        num //= 10
    return count


def num_tuple(tpl):
    num = 0
    for i in range(len(tpl)):
        num *= 10**(int_len(tpl[i]))
        num += tpl[i]
    return num


tpl = (1, 2, 385, 47, 5)
print(num_tuple(tpl))