from queue import *
#radix
#this little function is ripped straight from the book.
#It's use tis to find the Least Significant Digits by tossing items into queues
#instead of using a separate file from the internet (though that wouldn't be
#too hard) it will just be assortments of unsorted lists of strings that will be 
#sorted
def charAt(s,i):
    if len(s) - 1 < i:
        return " "
    return s[i]

def find_longest(los):
    longest = 0
    for item in los:
        if len(item) > longest:
            longest = len(item)
    return longest

def radixsort(unsortedlst, size):
    longest = find_longest(unsortedlst)
    
    mainQueue = Queue()
    queueList = [Queue() for i in range(256)]
    for item in unsortedlst:
        mainQueue.enqueue(charAt(item, longest))
    while not mainQueue.isEmpty():
        word = mainQueue.dequeue()
        
    

def main():
    alist = input("Please enter a list of words")
    alist = alist.split()
    radixsort(alist, len(alist))
    print(alist)
if __name__ == "__main__":
    main()