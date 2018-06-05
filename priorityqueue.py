class PriorityQueue:
    class __Node:
        def __init__(self, data, priority, next = None):
            self.data = data
            self.priority = priority
            self.next = next
        def getD(self):
            return self.data
        def setD(self, d):
            self.data = d
        def getP(self):
            return self.priority
        def setP(self,p):
            self.priority = p
        def getN(self):
            return self.next
        def setN(self,n):
            self.next = n
        def __repr__(self):
            return str(self.getD())
            
    def __init__(self):
        self.root = None
        self.count = 0
    def isEmpty(self):
        return self.count == 0
    def __len__(self):
        return self.count
    
    def enqueue(self,d,p):
        def __enqueue(root,d,p):
            if root == None:
                return PriorityQueue.__Node(d,p)
            newNode = PriorityQueue.__Node(d,p)
            if p > root.priority:
                newNode.next = root
                root = newNode
            else:
                current_node = root
                while p < current_node.priority and current_node.next != None:
                    current_node = current_node.next
                if current_node.next == None:
                    current_node.next = newNode
                    #return current_node
                if p > current_node.priority:
                    newNode.next = current_node
                    current_node = newNode
                    #return newNode
                
            return root
                
        self.root = __enqueue(self.root,d,p)
        self.count+=1
    def dequeue(self):
        temp = self.root
        self.root = self.root.next
        
        self.count -=1
        return temp
    def front(self):
        return str(self.root)
    def __repr__(self):
        return repr(list(self))
    def __iter__(self):
        current = self.root
        while current != None:
            yield current.getD()
            current = current.getN()
        
def main():
    p = PriorityQueue()
    p.enqueue("a",5)
    p.enqueue("c",7 )
    p.enqueue("b", 8)
    p.enqueue("d",4)
    p.enqueue("e", 9)
    p.enqueue("f", 3)
    p.enqueue("j", 10)
    print(p)
    print(p.dequeue())
    
if __name__ == "__main__":
    main()