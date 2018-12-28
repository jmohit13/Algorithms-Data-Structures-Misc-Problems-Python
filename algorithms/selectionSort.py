# Selection Sort

def selectionSort(theList):
    """
    Array is considered to be divided into two parts : unsorted and sorted
    
    Selection : Select the lowest element in the remaining array
    
    Swapping : Bring it to the starting position
    
    Counter shift : Change the counter for the unsorted array
    
    INPUT
    ---------
        theList : list
        
        Input : [54,26,93,17]
        Step 1 : [54, 26, 17, 93]
        Step 2 : [17, 26, 54, 93]
        
    
    """

    for i in range(len(theList)-1,1,-1):
        big_num = theList[0]; big_num_index = 0;
        for j in range(0,i):
            if theList[j] > big_num:
                big_num = theList[j]
                big_num_index = theList.index(theList[j])

        # Swapping
        temp = theList[i]
        theList[i] = big_num
        theList[big_num_index] = temp
    
    return theList
        




