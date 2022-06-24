def triangle_area(heigth, basis):
    return heigth * basis / 2


h = int(input("enter the height of triangle: "))
b = int(input("enter the length of basis: "))

print("triangle area is equal to", triangle_area(h, b))
