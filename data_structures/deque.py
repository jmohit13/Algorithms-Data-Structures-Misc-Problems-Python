# Deque

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
        self.items.insert(len(items),item)
        
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
        
if __name__ == "__main__":
    de = Deque()
    print(de)
    de.addRear(4)
    de.addRear('dog')
    print(de.items)
    print(de.size())
    print(de.isEmpty())
    print(de.addRear(8.4))
    print(de.items)
    print(de.removeRear())
    print(de.items)
    print(de.removeFront())
    print(de.items)