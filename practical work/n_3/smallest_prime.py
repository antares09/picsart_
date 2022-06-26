def is_clear(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def smallest_prime(n):
    num = n + 1
    i = 1
    while not is_clear(num):
        if num > n and is_clear(num):
            return num
        num += 1
    return num


num = 118
print(smallest_prime(num))