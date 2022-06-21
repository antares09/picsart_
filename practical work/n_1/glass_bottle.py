def price(small_bottle, big_bottle):
    s = 0
    while small_bottle > 0:
        small_bottle -= 1
        s += 0.10
    while big_bottle > 0:
        s += 0.25
        big_bottle -= 1
    return s


bottle_small = int(
    input("Enter how many small bottles you have (1 litre and lower): "))
bottle_big = int(
    input("Enter how many big bottles you have(higher than 1 litre): "))
print("total sum is $", f'{price(bottle_small, bottle_big):.2f}')