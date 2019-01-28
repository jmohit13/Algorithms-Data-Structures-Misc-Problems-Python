# Stack Implementation
import unittest

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


class StackTest(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def testPush(self):
        self.s.push(3)
        self.assertEqual(self.s.items[len(self.s.items)-1],3)

    def testPop(self):
        self.s.push(1)
        self.s.push(4)
        removedItem = self.s.pop()
        self.assertEqual(removedItem,4)

    def testPeek(self):
        self.s.push(1)
        self.s.push(5)
        self.assertEqual(self.s.peek(),5)

    def testSize(self):
        self.s.push(9)
        self.s.push(2)
        self.s.push(6)
        self.assertEqual(self.s.size(),3)

    def testIsEmpty(self):
        self.assertTrue(self.s.isEmpty())

if __name__ == "__main__":
    unittest.main()