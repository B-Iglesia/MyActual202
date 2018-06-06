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
            if float(p) >= float(root.priority):
                newNode.next = root
                root = newNode
            #elif float(p) == float(root.priority):
                    #newNode.next = root
                    #root = newNode
            else:
                root.setN(__enqueue(root.next,d,p))
            '''
            else:
                current_node = root
                while float(p) < float(current_node.priority) and current_node.next != None:
                    current_node = current_node.next
                
                    #return current_node
                if float(p) > float(current_node.priority):
                    newNode.next = current_node
                    current_node = newNode                
                    
                elif float(p) == float(current_node.priority) and float(p) > float(current_node.next.priority):
                    newNode.next = current_node.next
                    current_node.next = newNode
                else:
                    current_node.next = newNode                
            '''
            return root
                
        self.root = __enqueue(self.root,d,p)
        self.count+=1
    def dequeue(self):
        
        temp = self.root
        #if self.root.next == None:
            
        #    self.count -=1
            
        self.root = self.root.next
        
        self.count -=1
        return temp.data
    def front(self):
        if isinstance(self.root.data, list) or isinstance(self.root.data, tuple) or isinstance(self.root.data,int) or isinstance(self.root.data,bool):
            return self.root.data
        return str(self.root)
    def __repr__(self):
        return repr(list(self))
    def __iter__(self):
        current = self.root
        while current != None:
            yield current.getD()
            current = current.getN()
    def __len__(self):
        return self.count
def main():
    p = PriorityQueue()
    
    p.enqueue('a',5)
    p.enqueue('g',10)
    p.enqueue('c',15)
    p.enqueue('t',6)
    p.enqueue(list(),100)
    
    print(p.front(),"This")
    #while p:
        #p.dequeue()
        #print(p)
if __name__ == "__main__":
    main()