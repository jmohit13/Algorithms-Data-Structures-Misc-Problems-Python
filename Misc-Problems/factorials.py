def showMeTheFactorial(x):
    """
        Calculate factorial of number. 
        
        Γ(n) = (n−1)! for any positive integer n
        
        It can be also calulated as n! = (n+1)!/n i.e. 0! = 1! / 1 = 1
        
        4! = 4 x 3 x 2 x 1 = 24
        
        Factorial function can be generalized to the Gamma function. 
        The Gamma function can also be extended to complex numbers by replacing the real number x in the definition by a complex number z. 
        Gamma function is undefined for nonpositive integers, so factorial of a nonpositive integer can`t be calculated.
        
        INPUT
        -----------
        x : positive integer
        
    """
    def _fetch_product(theList):
        """
        INPUT
        --------
        list : [1,2,3,4]
        
        RETURN
        ---------
        list : [1*2,3,4]
        """
        tempList = []; 
        
        if len(theList) > 1:
            tempList.append(theList[0] * theList[1])
            for i in theList[2:len(theList)]:
                tempList.append(i)
        return tempList

    if x > 0:
        numList = [i for i in range(1,x+1)]
            
        while len(numList) > 1:
            print(len(numList),numList)
            numList = _fetch_product(numList)

        return numList[0]
    elif x == 0:
        return 1
    else:
        return 

