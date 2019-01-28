# Insertion Sort
import unittest

def insertionSort(theList):
    """
        Complexity : O(n^2)
        
        It always maintains a sorted sublist in the lower positions of the list. 
        Each new item is then inserted back into the previous sublist such that 
        the sorted sublist is one item larger.
        
        Step 1 : Select the first unsorted element
        Step 2 : Swap other elements to the right to create the correct position and shift the unordered element
        Step 3 : Advance the marker to the right one element
        
    INPUT 
    -----------
        theList : [7,8,5,2]
    RETURN
    -----------
        sorted list : [2,5,7,8]
        Steps : [7, 5, 8, 2], [5, 7, 8, 2], [5, 7, 2, 8], [5, 2, 7, 8], [2, 5, 7, 8]
    
    """
    
    for i in range(0,len(theList),1):
        for j in range(i+1,len(theList),1):
            while (j > 0):
                if theList[j] < theList[i]:
                    temp = theList[j]
                    theList[j] = theList[i]
                    theList[i] = temp
                j -= 1; i -= 1
            break
    return theList
    
class InsertionSortTest(unittest.TestCase):
    def test(self):
        self.l1 = [54,26,93,17,77,31,44,55,20]
        self.l2 = [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]
        self.assertListEqual(insertionSort(self.l1),[17, 20, 26, 31, 44, 54, 55, 77, 93])
        self.assertListEqual(insertionSort(self.l2),[4, 5, 8, 10, 12, 14, 15, 18, 19, 20])

if __name__ == "__main__":
    unittest.main()
    
