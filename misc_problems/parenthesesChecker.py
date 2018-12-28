import sys
sys.path.append('..')
from data_structures.stack import Stack

def parenthesesChecker(string):
    """
    Parentheses Checker validates the string using stack
    
    INPUT
    ---------
        string : '(()))'
    RETURN
    ---------
        Flag : False
    
    """
    temp = Stack(); balanceFlag = False
    
    for i in string:
        if i == "(":
            temp.push('i')
        if i == ")":
            if temp.isEmpty():
                balanceFlag = False
            else:
                temp.pop();
                balanceFlag = True
                
    if balanceFlag and temp.isEmpty():
        return True
    else:
        return False


if __name__ == "__main__":
    # print(parenthesesChecker('((()))'))
    print(parenthesesChecker('(()))'))