def mpg_l(mpg):
    return mpg * 235.22


mpg1 = int(input("Enter fuel consumption measured in miles-per-gallon(MPG): "))
print(" MPG converted to L'/'100km", mpg_l(mpg1))