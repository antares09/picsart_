def plot_square(width, length):
    return (width * length) / 43560


l = float(input("Enter the length in funts:  "))
w = float(input("Enter the width in funts: "))
print("Teritory square is", f'{plot_square(w,l):.3f}', "acres")