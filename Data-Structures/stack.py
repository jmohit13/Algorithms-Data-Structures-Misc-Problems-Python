# Stack Implementation

class Stack:
    """
        Stack maintain a LIFO property
        LIFO : last-in first-out
    """
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        """
            Tests to see whether the stack is empty.
            It needs no parameters and returns a boolean value.
        """
        return False if len(self.items) != 0 else True
        
    def push(self,item):
        """
            Adds a new item to the top of the stack. 
            It needs the item and returns nothing.
        """
        self.items.append(item)

    def pop(self):
        """
            Removes the top item from the stack. 
            It needs no parameters and returns the item. The stack is modified.
        """
        removed_item = self.items[len(self.items)-1]
        self.items.remove(self.items[len(self.items)-1])
        return removed_item
    
    def peek(self):
        """
            Returns the top item from the stack but does not remove it. 
            It needs no parameters. The stack is not modified.        
        """
        return self.items[len(self.items)-1]
    
    def size(self):
        """
            Returns the number of items on the stack.
            It needs no parameters and returns an integer.            
        """
        return len(self.items)