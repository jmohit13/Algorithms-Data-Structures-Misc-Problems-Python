# Queue Implementation
import unittest

class Queue:
    """
        Queue maintain a FIFO ordering property. 
        FIFO : first-in first-out
    """
    
    def __init__(self):
        self.items = []
        
    def enqueue(self,item):
        """
            Adds a new item to the rear of the queue. 
            It needs the item and returns nothing.
        """
#         temp_list = []; temp_list.append(item)
#         self.items = temp_list + self.items
        self.items.insert(0,item)
        
    def dequeue(self):
        """
            Removes the front item from the queue. 
            It needs no parameters and returns the item. The queue is modified.
        """
        return self.items.pop()
    
    def isEmpty(self):
        """
            Tests to see whether the queue is empty.
            It needs no parameters and returns a boolean value.
        """
        return self.items == []
        
    def size(self):
        """
            Returns the number of items in the queue.
            It needs no parameters and returns an integer.
        """
        return len(self.items)
    

class QueueTest(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def testEnqueue(self):
        self.q.enqueue('ball')
        self.assertEqual(self.q.items[0],'ball')

    def testDequeue(self):
        self.q.enqueue('baseball')
        removedItem = self.q.dequeue()
        self.assertEqual(removedItem,'baseball')

    def testIsEmpty(self):
        self.assertTrue(self.q.isEmpty())

    def testSize(self):
        self.q.enqueue('ball')
        self.q.enqueue('football')
        self.assertEqual(self.q.size(),2)

if __name__ == "__main__":
    unittest.main()

