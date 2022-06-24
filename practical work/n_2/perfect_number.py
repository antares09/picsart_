def divider(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]


def number_is_perfect(num):
    return True if sum(divider(num)) == num else False


number = int(input("enter the number: "))

if number_is_perfect(number):
    print("number is perfect")
else:
    print("number is not perfect")
