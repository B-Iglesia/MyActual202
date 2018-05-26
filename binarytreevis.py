from queue import *
from stack import *

class BinarySearchTree:
    class __Node:
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right
        def getVal(self):
            return self.val
        def setVal(self,newval):
            self.val = newval
        def getLeft(self):
            return self.left
        def getRight(self):
            return self.right
        def setLeft(self,newleft):
            self.left = newleft
        def setRight(self, newright):
            self.right = newright
        def contains(self, data):
            if self.val == data:
                return True
            elif self.val > data:
                if self.left:
                    return self.left.contains(data)
                else:
                    return False
            else:
                if self.right:
                    return self.right.contains(data)
                else:
                    return False
        #The smallest value will always be located to the left of the root, so
        #only goes down the left of the tree, traversing until
        #it hits "none" meaning that value is the smallest (no left leaf nodes)
        def minval(self):
            current = self
            parent = 0 
            while current.left is not None:
                parent = current
                current = current.left
                
                
            return current.getVal(), parent
        
        def rightminval(self):
            current = self
            while current.right is not None:
                current = current.right
                if current.left != None:
                    current = current.left
                    break
            return current.getVal()
        
        def largestval(self):
            if self.right == None:
                return self
            return self.right.largestval()
        #when a user deletes a value higher in a tree, the left child should
        #become the new val where the old one was.
        
        #Gets all items in ascending order. Does an inorder traversal
        #of the nodes of the tree
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem
            
            yield self.val
            
            if self.right != None:
                for elem in self.right:
                    yield elem
        
        def __repr__(self):
            return str(self.getVal())
        
        def levelorder(root):
            if root is None:
                return []
            q = Queue()
            q.enqueue(root)
            lol = []
            while not q.isEmpty():
                a = q.dequeue()
                if a.getLeft() != None:
                    q.enqueue(a.left)
                if a.getRight() != None:
                    q.enqueue(a.right)
                lol.append(a.getVal())
            return lol        
        
        def delete(self, val):
            if self.val == val:
                if self.right and self.left:
                    succ,parent = self.left.minvalue()
                    #find the successor of the node to be deleted, and 
                    if parent.right == succ:
                        parent.right = succ.left
                    else:
                        parent.left = succ.left
                    
                    succ.right = self.right
                    succ.left = self.left
                    
                    return succ
                else:
                    if self.left:
                        return self.left
                    return self.right
                
            else:
                if self.val > val:
                    if self.left:
                        self.left = self.left.delete(val)
                else:
                    if self.right:
                        self.right = self.right.delete(val)
            return self
                
        
        def preorder(self):
            pass
        
        def postorder(root):
            pass
            
        def inorder(self):
            pass
    def __init__(self, contents = []):
        self.root = None
        for i in contents:
            self.insert(i)

    def insert(self,val):
        
        #the __insert function is recursive and is not passed a self parameter. It is
        #a static function (not a method) but is hidden inside the insert function
        def __insert(root,val):
            if root == None:
                return BinarySearchTree.__Node(val)
            
            if val < root.getVal():
                root.setLeft(__insert(root.getLeft(),val))
            else:
                root.setRight(__insert(root.getRight(),val))
            
            return root
        self.root = __insert(self.root,val)
    
    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()
    
    def __contains__(self, data):
        return self.contains(data)
    
    def contains(self,data):
        if self.root:
            return self.root.contains(data)
        return False
    
    def delete(self, val):
        return self.root.delete(val)
    def minvalue(self):
        return self.root.minval()
    def rightminvalue(self):
        return self.root.rightminval()
    def largestval(self):
        if self.root.right == None:
            return root
        return self.root.largestval()
            
    
    def preorder(self):
        return self.root.preorder()
    def postorder(self):
        return self.root.postorder()
    def inorder(self):
        return self.root.inorder()
    def levelorder(self):
        return self.root.levelorder()




def main():
    tree = BinarySearchTree([10, 7, 13, 4, 8 , 12, 14,2,5,15])
    
 

    print(tree.minvalue())
    print(tree.rightminvalue())
    print(tree.largestval())
    tree.delete(2)
    print(2 in tree)
    for i in tree:
        print(i)
    print(tree.levelorder())
    print(tree.postorder())
    
if __name__ == "__main__":
    main()
