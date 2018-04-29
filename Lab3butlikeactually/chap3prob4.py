def swap(s):
    ss = ""
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s
    else:
        ss = ss + s[1]
        ss = ss + s[0]
    return ss + swap(s[2:])


print(swap("chicken"))
print(swap("turkey"))
print(swap("racecar"))
print(swap("Hello"))