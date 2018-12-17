# Stack Implementation

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return False if len(self.items) != 0 else True
        
    def push(self,item):
        self.items.append(item)

    def pop(self):
        removed_item = self.items[len(self.items)-1]
        self.items.remove(self.items[len(self.items)-1])
        return removed_item
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    