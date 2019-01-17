
"""
    Implementing Priority queue using Binary Heap

    A priority queue acts like a queue in that you dequeue an item by removing it from the front. 
    However, in a priority queue the logical order of items inside a queue is determined by their priority. 
    The highest priority items are at the front of the queue and the lowest priority items are at the back.
    
    Binary Heap : Enqueue and deque items in O(log n). It has two variation min heap, where the smallest key is in front
    Interesting property of complete tree is that we can represent it using a single list.
     
    Because tree is complete :-
        Left child of a parent, at position p, is the node that is found in position 2p
        Right child of the parent is at position 2p+1 in the list
        Parent of any node in the tree, we can simply use integer division

"""

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def percUp(self,i):
        """
            i : index of the element in list
        """
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i//2]
                self.heapList[i//2] = temp
            i = i // 2
    
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize); # self.percUp(len(self.heapList)-1)
    
    def percDown(self,i):
        """
            i : index of the element in list
        """
        while(2*i <= self.currentSize):
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
#             if self.heapList[2*i] < self.heapList[i]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[2*i]
                self.heapList[2*i] = temp
            i = mc
            
    def minChild(self,i):
        if 2 * i + 1 > self.currentSize:
            return 2 * i
        else:
            if self.heapList[2*i] < self.heapList[2*i+1]:
                return 2 * i
            else:
                return 2 * i + 1
    
    def delMin(self):
        """
            Remove the smallest, root node, then replace it with the last item in the list
            Then perc down that value to maintain the heap structure property
        """
        temp_val = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return temp_val
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
    
    
if __name__ == "__main__":
    bh = BinHeap()
    # bh.insert(5)
    # bh.insert(14)
    # bh.insert(27)
    # bh.insert(13)
    # bh.insert(11)
    # bh.insert(20)

    bh.buildHeap([9,5,6,2,3])
    print("Heaplist ",bh.heapList)
    print(bh.delMin())
    print("Heaplist ",bh.heapList)
    print(bh.delMin())
    print("Heaplist ",bh.heapList)