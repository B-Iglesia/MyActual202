from priorityqueue import *
from stack import *
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
    def isLeaf(self):
        if self.left == None and self.right == None:
            return True
        return False
    def twochildren(self):
        if self.left and self.right:
            return True
        return False
    def leftonly(self):
        if self.left and not self.right:
            return True
        return False
    def rightonly(self):
        if self.right and not self.left:
            return True
        return False
#this will take a string X of length n with d distinct characters
#and will return the huffman coding tree for X
'''=== Higher frequency characters have lower priority==='''
def huffman(X):
    
    Q = PriorityQueue()
    
    f = freq(X) #This is a dictionary
    c_sorted = sorted(f.items(), key=lambda x:ord(x[0]),reverse = True)
    
    for c in c_sorted:
        T = Node(c[1],c[0],None,None)
        Q.enqueue(T, 100-c[1])
    
    
    while len(Q) > 1:
        
        T1 = Q.dequeue()
        
        T2 = Q.dequeue()
        
        T = Node(T1.freq + T2.freq, str(T1.freq + T2.freq), T1, T2)
        pri = T1.freq + T2.freq
        
        Q.enqueue(T, 100-(pri))
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


def preorder(tree):
    root = tree
    b = []
    c = []
    a = []
    if not root:
        return
    if root.isLeaf():
        a = [root.char]
    if root.left:
        b = preorder(root.left)
    if root.right:
        c = preorder(root.right)
    return a + b + c
def findChar(ch,root):
    nodeS = Stack()
    moves = Stack()
    visited = []
    code = []
    nodeS.push(root)
    current_node = nodeS.top()
    while nodeS:
        if current_node.left and current_node.left not in visited:
            nodeS.push(current_node.left)
            visited.append(current_node.left)
            moves.push('L')
            current_node = nodeS.top()
        else:
            if current_node.right and current_node.right not in visited:
                nodeS.push(current_node.right)
                visited.append(current_node.right)
                moves.push('R')
                current_node = nodeS.top()
            if current_node.right in visited:
                moves.pop()
                nodeS.pop()
                current_node = nodeS.top()
        if current_node.isLeaf() and current_node.char != ch:
            moves.pop()
            nodeS.pop()
            current_node = nodeS.top()
        if current_node.isLeaf() and current_node.char == ch:
            while not moves.isEmpty():
                code.append(moves.pop())
            break
    
    return code[::-1]
def code_helper(code):
    cd = ''
    for i in code:
        if i == 'L':
            cd = cd + '0'
        else:
            cd = cd + '1'
    return cd
        
def get_huffman_code(ch,root):
    b = findChar(ch,root)
    return code_helper(b)


#Helper function for Huffman that will count the frequency of characters 
#i.e apple, p shows up twice, break ties for characters that have the same frequency by checking ASCII codes

        
    

def main():
    pass
    
    
if __name__ == '__main__':
    main()
