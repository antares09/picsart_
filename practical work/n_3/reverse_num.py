def reverse_num(num):
    rev = 0
    while num > 0:
        res = num % 10
        rev = rev * 10 + res
        num //= 10
    return rev


x = 12345
print(reverse_num(x))