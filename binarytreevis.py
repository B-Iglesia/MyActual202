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
        def minValue(self,node):
            current = node
            
            while current.left is not None:
                current = current.left
            
            return current
        
        def delete(self,data):
            if self is None:
                return None
            #determines where to search for the item in the left or right 
            #sub trees
            if data < self.val:
                self.left = self.left.delete(data)
            elif data > self.val:
                self.right = self.right.delete(data)
            
            else:
                #deletes a node with one child
                if self.left is None:
                    temp = self.right
                    self = None
                    return temp
                elif self.right is None:
                    temp = self.left
                    self = None
                    return temp
                
                #deleting a node with two children
                temp = self.minValue(self.right)
                self.val = temp.val
                self.right = self.right.delete(temp.val)
                
                
                
            return self
        
        def preorder(self):
            if self:
                print(str(self.val))
                if self.left:
                    self.left.preorder()
                if self.right:
                    self.right.preorder()
        
        def postorder(self):
            if self:
                if self.left:
                    self.left.postorder()
                if self.right:
                    self.right.postorder()
                print(str(self.val))
        
        def inorder(self):
            if self:
                if self.left:
                    self.left.inorder()
                print(str(self.val)) 
                if self.right:
                    self.right.inorder()
                       
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
    
    def delete(self,data):
        if self.root is not None:
            return self.root.delete(data)
            
    
    def preorder(self):
        print("PreOrder")
        self.root.preorder()
    
    def postorder(self):
        print("PostOrder")
        self.root.postorder()
    def inorder(self):
        print("InOrder")
        self.root.inorder()




def main():
    #s = input("Enter a list of numbers: ")
    #lst = s.split()
    tree = BinarySearchTree([1,3,4,2,6,5,8,7,9])
    
    #for x in lst:
        #tree.insert(float(x))
    #for x in tree:
       # print(x)
    tree.preorder()
    tree.postorder()
    tree.inorder()
    print(1 in tree)
    tree.delete(1)
    tree.delete(8)
    #tree.delete(9)
    #tree.delete(7)
    print(8 in tree , "me")
    print(9 in tree)
    print(7 in tree)
    
    #print(1 in tree)
if __name__ == "__main__":
    main()
