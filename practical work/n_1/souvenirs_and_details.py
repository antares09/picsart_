def _sum(s, d):
    sum1 = 0
    while s > 0:
        s -= 1
        sum1 += 112
    while d > 0:
        sum1 += 75
        d -= 1
    return sum1


suv = int(input("number of souvenirs: "))
det = int(input("number of small details: "))
print("total weigth: ", _sum(suv, det), "grams")