def quick_sort(lst):
    quick_sort2(lst,0,len(lst)-1)
def quick_sort2(lst, low, hi):
    if low<hi:
#p returns the pivot for the list
        p = partition(lst,low,hi)
        quick_sort2(lst,low,p-1)
        quick_sort2(lst,p+1,hi)

#We want the most middle value for the pivot
def get_pivot(lst,low,hi):
    mid = (hi + low) // 2
    pivot = hi
    if lst[low] < lst[mid]:
        if lst[mid]<lst[hi]:
            pivot = mid
    elif lst[low] < lst[hi]:
        pivot = low
    return pivot

def partition(lst,low,hi):
    pivotIndex = get_pivot(lst,low,hi)
    pivotValue = lst[pivotIndex]
    #swapping the values of the pivot and the low values
    lst[pivotIndex], lst[low] = lst[low], lst[pivotIndex]
    border = low
    for i in range(low, hi+1):
        if lst[i] <pivotValue:
            border +=1
            lst[i], lst[border] = lst[border], lst[i]
    lst[low], lst[border] = lst[border], lst[low]
    
    return border
l = [1,2,5,7,88,6,77,5,4,33,101,232,23,43,54,67,86,-1,-5,-44,57]
print(l)
quick_sort(l)
print(l)