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
        def find(self, data):
            if self.val == data:
                return True
            elif self.val > data:
                if self.left:
                    return self.left.find(data)
                else:
                    return False
            else:
                if self.right:
                    return self.right.find(data)
                else:
                    return False
        
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
    def __init__(self):
        self.root = None
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
    
    def find(self,data):
        if self.root:
            return self.root.find(data)
        return False
    
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
    s = input("Enter a list of numbers: ")
    lst = s.split()
    tree = BinarySearchTree()
    
    for x in lst:
        tree.insert(float(x))
    for x in tree:
        print(x)
    tree.preorder()
    tree.postorder()
    tree.inorder()

if __name__ == "__main__":
    main()
