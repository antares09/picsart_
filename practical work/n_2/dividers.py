def divider(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]


num = int(input("enter the number: "))
print(divider(num))
