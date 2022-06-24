lst = []
lst2 = []
mijin = 0
i = 0
print("enter the numbers: ")
while 1:
    lst.append(input(" "))
    if len(lst[i]) == 0:
        del lst[i]
        break
    i += 1
for i in range(len(lst)):
    lst2.append(int(lst[i]))
    mijin += lst2[i]

mijin /= len(lst)
lst3 = []
len = 0
for i in lst2:
    if i < mijin:
        lst3.append(i)

for i in lst2:
    if i == mijin:
        lst3.append(i)

for i in lst2:
    if i > mijin:
        lst3.append(i)

print(lst3)