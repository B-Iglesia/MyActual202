#this is the basic Stack Class code given by the text book
class Stack: 
    def __init__(self):
        self.items = []
    def pop(self):
        if self.isEmpty():
            raise RunTimeError("Attempt to pop an empty stack")
        
        topIdx = len(self.items) - 1
        item = self.items[topIdx]
        del self.items[idx]
        return item
    
    def push(self, item):
        self.items.append(item)
    def top(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to get top of empty stack")
        topIdx = len(self.items)-1
        return self.items[topIdx]
    def isEmpty(self):
        return len(self.items) ==0