import sys

#This first function is the actual merge_sort function
def merge_sort(lst):
    merge_sort2(lst,0,len(lst)-1)

#This is the recursive call for the merge_sort 
#It will DIVIDE AND CONQUER the list into smaller lists of half the size until
#both lists are of length one...
def merge_sort2(lst,start,end):
    if start < end:
        middle = (start + end) // 2
        merge_sort2(lst,start,middle)
        merge_sort2(lst,middle+1,end)
        merge(lst,start,middle,end)
#THEN the sublists will all have to be appended back to eachother (after subsequent
#recreation of the lists.
#Each sublist will have it's parts compared to eachother in order to sort the list
#The newly generated list will have all of the original numbers put in ascending 
#order
def merge(lst,start,middle,end):
    L=lst[start:middle+1]
    R=lst[middle+1:end+1]
#Provides and extra dummy index for the list so that the function knows where
#to stop
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i=j=0
    for k in range(start, end+1):
        if L[i] <= R[j]:
            lst[k] = L[i]
            i+=1
        else:
            lst[k] = R[j]
            j+=1
    
        
        
l = [1,2,5,7,88,6,77,5,4,33,101,232,23,43,54,67,86,-1,-5,-44,57]
print(l)
merge_sort(l)
print(l)