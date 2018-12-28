class BinaryTree:
    """
        Binary tree with left subtree and right subtree
    """
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            tempTree = BinaryTree(newNode)
            tempTree.leftChild = self.leftChild
            self.leftChild = tempTree
    
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            tempTree = BinaryTree(newNode)
            tempTree.rightChild = self.rightChild
            self.rightChild = tempTree
    
    def getRootVal(self):
        return self.key
    
    def setRootVal(self,newVal):
        self.key = newVal
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild