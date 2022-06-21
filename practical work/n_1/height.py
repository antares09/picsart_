def height_cm(funt, dyuym):
    cm = 0
    while funt > 0:
        funt -= 1
        dyuym += 12
    while dyuym > 0:
        cm += 2.54
        dyuym -= 1
    return cm


f = int(input("enter your height funt: "))
d = int(input("and dyuym: "))
print("your height in cantimetres: ", f'{height_cm(f, d):.3f}', "cm")
