import math


def circle_square(radius):
    return math.pi * radius**2


def volume_cylinder(radius, heigth):
    s = circle_square(radius)
    return s * h


r = int(input("enter the radius: "))
h = int(input("enter the height: "))
print("the volume is:", f'{volume_cylinder(r,h):.2f}')