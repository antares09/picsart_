import random

lst = []
k = random.randint(0, 999999)
print(k)
str = str(k)
for i in range(len(str)):
    lst.append(int(str[i]))
lst1 = sorted(lst)
print(lst1)