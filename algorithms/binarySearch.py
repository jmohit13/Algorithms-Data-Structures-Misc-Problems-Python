# Binary search
# 
# Best-case performance   O(1)
# Average performance O(log n)
# Worst-case space complexity O(1)

import math
import unittest

def binarySearch(l,item):
    """
    INPUT
    ---------
        l : list
        item : item to search in the list
    
    RETURN
    ---------
        itemFound : Flag indicating True or False
    """
   
    l.sort() # sort the list
    first = 0; last = len(l) - 1
    itemFound = False
    
    while(first <= last and itemFound is False):
        midpoint = int(math.floor((first + last)/2))
        if item == int(l[midpoint]):
            itemFound = True
        else:
            if item < l[midpoint]:
                last = midpoint - 1 # Update the last pointer
            else:
                first = midpoint + 1 # Update the first pointer
                
    return itemFound


class BinarySearchTest(unittest.TestCase):
    def testBinarySearch(self):
        self.l = [0, 1, 2, 8, 13, 17, 19, 32, 42]
        self.assertEqual(binarySearch(self.l, 2),True)

if __name__ == "__main__":
    unittest.main()