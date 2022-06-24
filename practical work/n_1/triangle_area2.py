import math


def triangle_area(side1, side2, side3):
    p = (side1 + side2 + side3) / 2
    return math.sqrt(p * (p - side1) * (p - side2) * (p - side3))


s1 = int(input("enter the first side of triangle: "))
s2 = int(input("enter the second side of triangle: "))
s3 = int(input("enter the second side of triangle: "))

print("triangle area is equal to", f'{triangle_area(s1,s2,s3):.2f}')
