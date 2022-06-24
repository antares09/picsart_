i = 0
lst = []
lst2 = []
while 1:
    lst.append(input("word: "))
    if lst[0] == 0:
        print("wrong input")
        break
    elif len(lst[i]) == 0:
        break
    i += 1

i = 0
for k in lst:
    if k not in lst2:
        lst2.append(k)

for i in range(len(lst2)):
    print(lst2[i])