# Deque
import unittest

class Deque:
    """
        A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue.
        It has two ends, a front and a rear, and the items remain positioned in the collection.
        New items can be added/removed at either the front or the rear.
        This hybrid linear structure provides all the capabilities of stacks and queues in a single data structure.
        It does not require the LIFO and FIFO orderings that are enforced by stacks and queues data structures.
         
    """
    def __init__(self):
        self.items = []
        
    def addFront(self,item):
        self.items.insert(len(self.items),item)
        
    def addRear(self,item):
        self.items.insert(0,item)
        
    def removeFront(self):
        return self.items.pop()
        
    def removeRear(self):
        return self.items.pop(0)
        
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
        

class DequeTest(unittest.TestCase):
    def setUp(self):
        self.dq = Deque()
 
    def testAddFront(self):
        self.dq.addFront(4)
        self.assertEqual(self.dq.items[len(self.dq.items)-1],4)

    def testAddRear(self):
        self.dq.addRear('shell')
        self.assertEqual(self.dq.items[0],'shell')

    def testRemoveFront(self):
        self.dq.addRear('dog')
        self.dq.addFront('cat')
        itemRemoved = self.dq.removeFront()
        self.assertEqual(itemRemoved,'cat')

    def testRemoveRear(self):
        self.dq.addRear('dog')
        self.dq.addFront('cat')
        itemRemoved = self.dq.removeRear()
        self.assertEqual(itemRemoved,'dog')

    def testIsEmpty(self):
        self.assertTrue(self.dq.isEmpty())

    def testSize(self):
        self.assertEqual(self.dq.size(),0)


if __name__ == "__main__":
    unittest.main()
