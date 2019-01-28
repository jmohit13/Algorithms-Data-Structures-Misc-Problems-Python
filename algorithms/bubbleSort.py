# Bubble Sort
import unittest

def bubbleSort(theList):
    """
    The highest element bubbles to the top in each loop.
    
    Complexity
        Worst case : O(n^2)
        Best case : O(n)
    
    INPUT 
    -----------
        theList : [5,1,4,2,8,9]

    RETURN
    -----------
        sorted list : [1, 2, 4, 5, 8, 9]
        
        Step 1 : [1, 5, 4, 2, 8, 9], 
        Step 2 : [1, 4, 5, 2, 8, 9], 
        Step 3 : [1, 4, 2, 5, 8, 9], 
        Step 4 : [1, 2, 4, 5, 8, 9]
    
    """
    
    for i in range(len(theList)-1,0,-1):
        for j in range(0,i,1):
            if theList[j+1] < theList[j]:
                temp = theList[j]
                theList[j] = theList[j+1]
                theList[j+1] = temp
                
    return theList

class BubbleSortTest(unittest.TestCase):
    def testBubbleSort(self):   
        self.l1 = [5,1,4,2,8,9]
        self.l = [54,26,93,17,77,31,44,55,20]
        self.assertListEqual(bubbleSort(self.l),[17, 20, 26, 31, 44, 54, 55, 77, 93])
        self.assertListEqual(bubbleSort(self.l1),[1,2,4,5,8,9])

if __name__ == "__main__":
    unittest.main()
