def is_palindrom(sentence):
    str = sentence.lower()
    str = str.replace(",", "")
    lst = str.split(" ")
    for i in range(len(lst) // 2):
        if lst[i] != lst[len(lst) - 1 - i]:
            return "Not palindrom"  #False
    return "palindrom"  #True


str = input("enter the sentence: \n")
print("your sentence is", is_palindrom(str))
