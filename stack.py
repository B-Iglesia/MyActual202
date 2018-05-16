#this is the basic Stack Class code given by the text book
class Stack: 
    def __init__(self):
        self.items = []
    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop an empty stack")
        
        topIdx = len(self.items) - 1
        item = self.items[topIdx]
        del self.items[topIdx]
        return item
    
    def push(self, item):
        self.items.append(item)
    def top(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to get top of empty stack")
        topIdx = len(self.items)-1
        return self.items[topIdx]
    def isEmpty(self):
        return len(self.items)==0
    def __repr__(self):
        print(str(self.items))
    
    def __iter__(self):
        for item in self.items:
            yield item