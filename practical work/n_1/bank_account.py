def savings(money, years=1):
    sum1 = money
    while years > 0:
        sum1 = sum1 + (sum1 * 4) / 100
        years -= 1
    return sum1


money = int(input("your bank savings: "))

print("your savings after 1 year: ", savings(money))
print("your savings after 2 year: ", savings(money,2))
print("your savings after 3 year: ", savings(money,3))