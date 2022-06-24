i = 0
lst = []
while 1:
    lst.append(int(input("number: ")))
    if lst[0] == 0:
        del lst[0]
        print("wrong number")
        break
    elif lst[i] == 0:
        del lst[i]
        break
    i += 1

s = 0
for k in lst:
    s += k
if lst:
    print("average is", f'{s/len(lst):.3f}')