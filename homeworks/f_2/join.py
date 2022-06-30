def join(data, sep):
    str = ''
    for i in data:
        str += i
        str += sep
    return str[:len(str) - len(sep)]


print(join(["hey", "lll", "lok", "gg"], " joy "))
