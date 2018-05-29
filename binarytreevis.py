from queue import *
from stack import *
from turtle import *
import tkinter.messagebox
import tkinter
from tkinter import *
screenMin = 0
screenMax = 300
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
            elif self.getVal() > data:
                if self.left:
                    return self.left.contains(data)
                else:
                    return False
            else:
                if self.right:
                    return self.right.contains(data)
                else:
                    return False
        def two_children(self):
            if self.left != None and self.right != None:
                return True
            return False
        def no_children(self):
            if self.left == None and self.right == None:
                return True
            return False
        def one_child(self):
            if self.left != None and self.right == None:
                return self.left
            return self.right
        #The smallest value will always be located to the left of the root, so
        #only goes down the left of the tree, traversing until
        #it hits "none" meaning that value is the smallest (no left leaf nodes)
        def minval(self):
            current = self
            
            while current.left is not None:
                
                
                current = current.left
                
            return current
        
        def rightminval(self):
            while self.left != None:
                self = self.left
            return self
        
        def largestval(self):
            if self.right:
                return self.right.largestval()
            return self
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
        def delete_helper(self, val):
            if self == None or self.val == None:
                return self
            elif val < self.getVal():
                if self.left != None:
                    self.left = self.left.delete_helper(val)
            elif val > self.getVal():
                if self.right != None:
                    self.right = self.right.delete_helper(val)
            else:
                if self.no_children():
                    del(self)
                    self = None
                    
                elif self.left == None:
                    temp = self.right.minval()
                    self.setVal(temp.getVal())
                    self.right = self.right.delete_helper(temp.getVal())
                    del(temp)
                elif self.right == None:
                    temp = self.left.minval()
                    self.setVal(temp.getVal())
                    self.left = self.left.delete_helper(temp.getVal())
                    del(temp)
                else:
                    temp = self.right.minval()
                    self.setVal(temp.getVal()) 
                    self.right = self.right.delete_helper(temp.getVal())
            return self
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
                if i is not None:
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
    
    
    
    def delete(self, val):
            
        return self.root.delete_helper(val)
    def __contains__(self, data):
        return self.contains(data)
    
    def contains(self,data):
        if self.root:
            return self.root.contains(data)
        return False    
    def minvalue(self):
        return self.root.minval()
    def rightminvalue(self):
        return self.root.rightminval()
    def largestval(self):
        if self.root.right == None:
            return self.root
        return self.root.largestval()
            
    
    def preorder(self):
        return self.root.preorder()
    def postorder(self):
        return self.root.postorder()
    def inorder(self):
        return self.root.inorder()
    def levelorder(self):
        return self.root.levelorder()


class BSTVis(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.pack()
        self.buildWindow()    
        self.paused = False
        self.stop = False
        self.running = False
        self.locked = False
    def buildWindow(self):
        cv = ScrolledCanvas(self, 600,600,600,600)
        cv.pack(side = tkinter.LEFT)
        t = RawTurtle(cv)
        screen = t.getscreen()
        screen.tracer(100000)
        
        screen.setworldcoordinates(screenMin,screenMin,screenMax,screenMax)
        screen.bgcolor("white")
        t.ht()
        
        frame = tkinter.Frame(self)
        frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
        
        def quitHandler():
            self.master.quit()
        quitButton = tkinter.Button(frame, text = "Quit", command =quitHandler)
        quitButton.pack()
        
        def entryHandler():
            pass
        e = Entry(frame)
        e.pack()
        
        insertButton = tkinter.Button(frame, text = "Insert")
        insertButton.pack()
        
        containsButton = tkinter.Button(frame,text = "Contains?")
        containsButton.pack()
        
        
def main():
    tree = BinarySearchTree(contents = [10, 7, 13, 4, 8,7.5,12, 14,2,5,15, 16])
    tree2 = BinarySearchTree(contents=[0, 1, 2])
    tree3 = BinarySearchTree(contents=[0,1,2,3,4,5])
    tree2.delete(0)
    print(tree2.delete(0))
    print(0 in tree2)
    
    for i in tree2:
        print(i)
 #   print(tree2.levelorder())
  #  tree.delete(15)
    
#    rot = tkinter.Tk()
 #   rot.title("Binary Search Tree Visualizer")
  #  application = BSTVis(rot)
   # application.mainloop()
    print(tree.levelorder(), "levelorder")
    #print(tree.inorder(), "inorder")
    #print(tree.preorder(), "preorder")
    #print(tree.postorder(), "postorder")
if __name__ == "__main__":
    main()
