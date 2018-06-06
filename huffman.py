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
    def __iter__(self):
        if self.left != None:
            for elem in self.left:
                yield elem
        
        yield self.char
        
        if self.right != None:
            for elem in self.right:
                yield elem    
#this will take a string X of length n with d distinct characters
#and will return the huffman coding tree for X
'''=== Higher frequency characters have lower priority==='''
def huffman(X):
    
    Q = PriorityQueue()
    
    f = freq(X) #This is a dictionary
    c_sorted = sorted(f.items(), key=lambda x:ord(x[0]),reverse = True)
    print(c_sorted)
    for c in c_sorted:
        T = Node(c[1],c[0],None,None)
        Q.enqueue(T, 100-c[1])
    
    
    while len(Q) > 1:
    
        T1 = Q.dequeue()
       
        T2 = Q.dequeue()
        
        T = Node(T1.freq + T2.freq, str(T1.freq + T2.freq), T2, T1)
        
        Q.enqueue(T, 100-(T1.freq + T2.freq))
    
    T = Q.dequeue()
    
    return T
def freq(c):
    dict = {}
    for n in c:
        keys = dict.keys()
        if n in keys:
            dict[n] +=1
        else:
            dict[n] = 1
    return dict

''' If you traverse left, "0", if you traverse right
"1" get the code when you reach the character and return that code number (or probably the
the code numbers in a list
'''

def code_generator(n,li):
    code = ""
    if n > 0:
        code = code + '1'*n
    code = code + '0'
    if n+1 == len(li):
        code = code[:len(li)-1]
    return code
def get_huffman_code(ch,root):
    n = [i for i in root]
    chars = []
    for i in range(len(n)-1):
        chars.append(n[i].char)    
    m = sorted(chars)
    codes = []
    for i in range(len(n)):
        codes.append(code_generator(i,n))
    idx = 0
    for i in chars:
        if i == ch:
            break
        idx +=1
    return codes[idx]

def get_huffman_codes(ch, root):
    n = tree_traverse(root)
    codes = []
    for i in range(len(n)):
        codes.append(code_generator(i,n))
    dict = {}
    chars = []
    for i in range(len(n)-1):
        chars.append(n[i].char)
    chars.append(n[len(n)-1].char)
    
    for i in range(0,len(n)):
        dict[chars[i]] = codes[i]
    return dict

#Helper function for Huffman that will count the frequency of characters 
#i.e apple, p shows up twice, break ties for characters that have the same frequency by checking ASCII codes

        
    

def main():
    #sent = "aaaaajjjjjdddkkllllllff"
    #a = huffman("aaaaajjjjjdddkkllllllff")
    sent = "aaaaggccttt"
    a = huffman(sent)
    for i in a:
        print(i)
    #print(a.left.right)
    #print(tree_traverse(a))
    #print(get_huffman_code(sent,a))
    sent = 'asdf;k;lkjasdfk dasiirFFDg'
    a = huffman(sent)
    #for i in a:
    #    print(i)
    #print(tree_traverse(a))
    #print(get_huffman_codes(sent,a))
    
    
if __name__ == '__main__':
    main()
