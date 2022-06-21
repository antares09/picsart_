def room_square(width, length):
    return width * length


w = float(input("Enter the width: "))
l = float(input("Enter the length: "))
print("Room square is", room_square(w, l), "meters")