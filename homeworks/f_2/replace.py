def replace(source, old, new, count=-1):
    lst = [None] * len(old)
    result = []
    l_old = list(old)
    l_source = list(source)
    c_count = 0
    result = []
    res = []
    l = 0
    for j in range(len(l_source) - len(old)):
        lst = [None] * len(old)
        for i in range(len(old)):
            lst[i] = l_source[l]
            l += 1
        l -= len(old) - 1
        if lst == l_old and c_count < count:
            c_count += 1
            result.extend(l_source[:j])
            result.extend(list(new))
            result.extend(l_source[j + len(old):])
            break
    if c_count < count:
        return (replace(''.join(result), old, new, c_count))
    return ''.join(result)


str = "hell well bell there hell hell"
print(replace(str, "hell", "heaven", 2))
