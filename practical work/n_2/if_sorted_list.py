def is_sorted(lst):
    lst1 = sorted(lst, reverse=True)
    lst2 = sorted(lst, reverse=False)
    return True if lst2 == lst or lst1 == lst else False


str = input("enter the list of numbers: \n")
lst1 = str.split(" ")
lst = []
for i in range(len(lst1)):
    lst.append(int(lst1[i]))
if is_sorted(lst):
    print("Your list is sorted")
else:
    print("Your list is not sorted")