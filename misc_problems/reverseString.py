import sys
sys.path.append('..')
from data_structures.stack import Stack

def reverseString(mystr):
    """
    Reverses the input string using Stack data structure
    
    INPUT
    -------
        mystr : apple
    RETURN
    -------
        elppa
        
    """
    revStr = ''; temp = Stack()
   
    for token in mystr: temp.push(token)
    
    for i in range(temp.size()):
        revStr += temp.pop()
    
    return revStr
    
if __name__ == "__main__":
    print(reverseString('apple'))
    

