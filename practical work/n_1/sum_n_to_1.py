def _sum(num):
    if num == 1:
        return 1
    else:
        return num + _sum(num - 1)


n = int(input("Enter the number: "))
print(_sum(n))