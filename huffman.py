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
        Q.enqueue(T, 100-(ord(c)*f[c]))
   
    while len(Q) > 1:
    
        T1 = Q.dequeue()
        T2 = Q.dequeue()
        T = Node(T1.data.freq + T2.data.freq, str(T1.data.freq + T2.data.freq), T2, T1)
    
        Q.enqueue(T, 100 - (T1.data.freq + T2.data.freq))
    
    T = Q.dequeue()
    
    return T.data

''' If you traverse left, "0", if you traverse right
"1" get the code when you reach the character and return that code number (or probably the
the code numbers in a list
'''
def tree_traverse(root):
    n = []
    while root.right != None:
        temp = root
        #print(root)
              
        root = root.right.data
        
        n.append(temp.left)
        if root.right == None:
            break          
    n.append(root)
    return n
def code_generator(n,li):
    code = ""
    if n > 0:
        code = code + '1'*n
    code = code + '0'
    if n+1 == len(li):
        code = code[:len(li)-1]
    return code
def get_huffman_code(ch, root):
    n = tree_traverse(root)
    codes = []
    for i in range(len(n)):
        codes.append(code_generator(i,n))
    dict = {}
    chars = []
    for i in range(len(n)-1):
        chars.append(n[i].data.char)
   
    chars.append(n[len(n)-1].char)
    
    for i in range(0,len(n)):
        dict[chars[i]] = codes[i]
    return dict

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
    sent = "aaaaajjjjjdddkkllllllff"
    a = huffman("aaaaajjjjjdddkkllllllff")
    
    print(get_huffman_code(sent,a))
    #print()
    #print()
    #print(a)
    #print(a.left.data)
    #print(a.right.data)
    #print(a.right.data.left.data)
    #print(a.right.data.right.data)
    #print(a.right.data.right.data.left.data)
    #print(a.right.data.right.data.right.data)
    #print(a.right.data.right.data.right.data.left.data)
    #print(a.right.data.right.data.right.data.right.data)
    #print(a.right.data.right.data.right.data.right.data.left.data)
    #print(a.right.data.right.data.right.data.right.data.right)
if __name__ == '__main__':
    main()
