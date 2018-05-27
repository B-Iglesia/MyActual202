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
            parent = self 
            while current.left is not None:
                parent = current
                
                current = current.left
                
            return current, parent
        
        def rightminval(self):
            current = self
            parent = self
            while current.right is not None:
                parent = current
                current = current.right
                if current.left != None:
                    current = current.left
                    break
            return current, parent
        
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
                    succ,parent = self.left.rightminval()
                    #find the successor of the node to be deleted, and 
                    if parent.left == succ:
                        parent.left = succ.right
                    else:
                        parent.right = succ.right
                    
                    succ.left = self.left
                    succ.right = self.right
                    
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
            root = self
            b = []
            c = []
            if not root:
                return
            a = [root.getVal()]
            if root.left:
                b = root.left.preorder()
            if root.right:
                c = root.right.preorder()
            return a + b + c
        
        def postorder(self):
            root = self
            a = []
            b = []
            if not root:
                return
            if root.left:
                a = root.left.postorder()
            if root.right:
                b = root.right.postorder()
            c = [root.getVal()]
            return a + b + c
            
            
        def inorder(self):
            ordered = []
            for i in self:
                ordered.append(i)
            return ordered
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
    tree = BinarySearchTree(contents = [10, 7, 13, 4, 8,12, 14,2,5,15])
    
 

    #print(tree.minvalue())
    #print(tree.rightminvalue())
    #print(tree.largestval())
    #tree.delete(10)
    #tree.delete(7)
    print(7 in tree)
    print(10 in tree, "I should not be here FUUUUUUUUUUUUCK")
    #tree.delete(2)
    #tree.delete(4)
    print(2 in tree)
    print(tree.levelorder(), "levelorder")
    print(tree.inorder(), "inorder")
    print(tree.preorder(), "preorder")
    print(tree.postorder(), "postorder")
if __name__ == "__main__":
    main()
