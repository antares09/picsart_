def split(source, sep):
    res = []
    indx = 0
    for i in range(len(source)):
        if source[i:i + len(sep)] == sep:
            res.append(source[indx:i])
            indx = i + len(sep)
        if not sep in source[indx:len(source)]:
            res.append(source[indx:len(source)])
            break
    return res


s = "kk slk; dkl; dlkf; dkljf"
print(split(s, '; '))
