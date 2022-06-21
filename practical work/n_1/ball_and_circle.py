import math


def circle_square(radius):
    return math.pi * radius**2


def ball_volume(radius):
    return 4 / 3 * (math.pi * radius**3)


r = int(input("enter the radius: "))
print("the circle square: ", f'{circle_square(r):.3f}')
print("the ball volume: ", f'{ball_volume(r):.3f}')