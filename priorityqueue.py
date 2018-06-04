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
            temp = PriorityQueue.__Node(d,p)
            if p > root.priority:
                
                temp.next = root
                root = temp
            else:
                while root.next != None and root.next.priority < p:
                    root = root.next
                
                temp.next = root.next
                root.next = temp
            return root
        self.root = __enqueue(self.root,d,p)
        self.count+=1
    def dequeue(self):
        temp = self
        self.root = self.root.getN()
        
        self.count -=1
        return temp
    def front(self):
        return str(self.root)
    def __repr__(self):
        return repr(list(self))
    def __str__(self):
        return str(list(self))
    def __iter__(self):
        current = self.root
        while current != None:
            yield current.getD()
            current = current.getN()
        
def main():
    p = PriorityQueue()
    for i in range(11):
        p.enqueue(i**2,i**2)
    print(p.count)
    print(p)
    p.dequeue()
    print(p)
    print(p.front())
    while p:
        print(p.dequeue())
    print(p)
    print(p.isEmpty())
if __name__ == "__main__":
    main()