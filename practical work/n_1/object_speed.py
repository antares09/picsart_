import math


def end_speed(d):
    v_0 = 0
    g = 9.8
    return math.sqrt(v_0**2 + 2 * g * d)


h = int(input("enter the height: "))
print("The speed of the object at the moment of reaching the ground",
      f'{end_speed(h):.3f}', "m/sec")