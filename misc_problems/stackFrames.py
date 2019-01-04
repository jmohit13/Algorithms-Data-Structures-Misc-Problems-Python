# Stack Frames Recursion
import sys
sys.path.append('..')
from data_structures.stack import Stack

def toStr(n,base):
    """
    Convert given number to number in different base
    
    Instead of concatenating the result of the recursive call to toStr with the string 
    from stringMap, Push the strings onto a stack instead of making the recursive call
        
    INPUT
    -------
        n : Input number eg 1453
        base : base to convert the number to eg. 16 or Hexadecimal
    RETURN
    -------
        newStr = (1453,16) => 5AD
    """
    
    tempStack = Stack(); stringMap = '0123456789ABCDEF'
    newStr = ''

    while (n > 0):
        quotient = n//base
        remainder = n % base
        if remainder > 9:
            tempStack.push(stringMap[remainder])
        else:
            tempStack.push(remainder)
        
        n = n // base
    
    while not tempStack.isEmpty():
        newStr += str(tempStack.pop())

    return newStr
    

if __name__ == "__main__":
    # print(toStr(1453,16)) # 5AD
    print(toStr(61453,16)) # 0xF00D
