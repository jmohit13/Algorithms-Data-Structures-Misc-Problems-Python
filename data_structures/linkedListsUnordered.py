# Unordered List : Linked Lists Implementation

"""
	Unordered List 

	We need to be sure that we can maintain the relative positioning of the items.
	If we can maintain some explicit information in each item, the location of the
	next item, then the relative position of each item can be expressed by
	simply following the link from one item to the next.
"""

class Node:
	"""
		Each node object must hold at least two pieces of information. 
		First, the node must contain the list item itself, the data field of the node.
		Second, each node must hold a reference to the next node.
	"""
	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data
        
	def setData(self,newdata):
		self.data = newdata
        
	def getNext(self):
		return self.next
        
	def setNext(self,newnext):
		self.next = newnext
        

class UnorderedList:
	
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        ptr = self.head; nodeCounter = 0
        
        while(ptr != None):
            ptr = ptr.getNext()
            nodeCounter += 1
            
        return nodeCounter
    
    def search(self,item):
        ptr = self.head; isPresent = False
        
        while ptr != None and not isPresent:
            if item == ptr.getData():
                isPresent = True
            else:
                ptr = ptr.getNext()
        return isPresent
    
    def remove(self,item):
        ptr = self.head; isPresent = False; previous = None
        
        while ptr != None and not isPresent:
            if item == ptr.getData():
                previous.setNext(ptr.getNext())
                ptr = None
                isPresent = True
            else:
                previous = ptr
                if ptr.getNext() != None:
                    ptr = ptr.getNext()
                else:
                    ptr = None

    
if __name__ == "__main__":
	mylist = UnorderedList()
	print(mylist.head)
	print("Is Linked List Empty ",mylist.isEmpty())
	mylist.add(31)
	mylist.add(77)
	mylist.add(47)
	mylist.add(17)
	print("Is Linked List Empty ",mylist.isEmpty())
	print("Linked List Size ",mylist.size())
	print("Looking for 17 ",mylist.search(17))
	print("Removed 31 ",mylist.remove(31))
	print("Looking for 31 ",mylist.search(31))

