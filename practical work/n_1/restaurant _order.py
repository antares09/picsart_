def taxes(money):
    return (money * 20) / 100


def tips(money):
    return (money - taxes(money)) * 18 / 100


order = int(input("Enter restaurant order amount: "))
print("Tax: ", f'{taxes(order):.2f}')
print("Tips: ", f'{tips(order):.2f}')
print("Total amount of money", f'{order+taxes(order)+tips(order):.2f}')