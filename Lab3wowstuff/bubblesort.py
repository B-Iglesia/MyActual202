def bubbleSort(lst):
    for i in range (0,len(lst)-1):
        for j in range(0,len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

l = [1,2,5,7,88,6,77,5,4,33,101,232,23,43,54,67,86,-1,-5,-44,57]
print(l)
bubbleSort(l)
print(l)