def intpow(x, n):
    if n == 0:
        return 1
    return x * intpow(x, n-1)
print(intpow(2,4)) #16
print(intpow(3,3))#27
print(intpow(4,3))#64
print(intpow(5,2)#25