from priorityqueue import *

'''
Just the steps interpreted from the code doc
1. Huffman takes a string called X with length N and D distinct characters
2. Compute the frequency for each character C in X
3. Make a priority Queue, Q
4.for each character c, make a single node binary tree storing c with
detail about its frequency

5. Use the Queue to dequeue and start left and right subtree, then insert new tree into Q with combined frequency
6. Finally, dequeue the last item (which should be the entire huffman encoded tree)
7. Return Tree
'''
class Node:
    def __init__(self,freq,char,left,right):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    def __repr__(self):
        return str((self.char, self.freq))
#this will take a string X of length n with d distinct characters
#and will return the huffman coding tree for X
'''=== Higher frequency characters have lower priority==='''
def huffman(X):
    X.lower()
    Q = PriorityQueue()
    f = freq(X) #This is a dictionary
    for c in f:
        T = Node(f[c],c,None,None)
        Q.enqueue(T, 100-(f[c]*ord(c)))
    while Q:
        T1 = Q.dequeue()
        print(type(T1))
        T2 = Q.dequeue()
        #T = Node(None, T1.freq + T2.freq, T1, T2)
        print(T)
        Q.enqueue(T, 100 - T.freq)
        print(Q)
    
#Helper function for Huffman that will count the frequency of characters 
#i.e apple, p shows up twice, break ties for characters that have the same frequency by checking ASCII codes
def freq(c):
    dict = {}
    for n in c:
        keys = dict.keys()
        if n in keys:
            dict[n] +=1
        else:
            dict[n] = 1
    return dict
        
        
    

def main():
    print(huffman("aaaaaffffjjjkllloooooo"))
if __name__ == '__main__':
    main()
