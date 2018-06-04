from priorityqueue import *

'''
Just the steps interpreted from the code doc
1. Huffman takes a string called X with length N and D distinct characters
2. Compute the frequency for each character C in X
3. Make a priority Queue, Q
4.for each character c, make a single node binary tree story c with
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
'''=== Higher frequency characters have lower priorty==='''
def huffman(X):
    Q = PriorityQueue()
    f = freq(X) #This is a dictionary
    n = []
    for k in f:
        n.append(Node(f[k],k,k,k))
    for i in n:
        Q.enqueue(i,ord(i.char)*i.freq)
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
    print(huffman("hello"))
if __name__ == '__main__':
    main()