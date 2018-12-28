# Tree

"""
    A tree consists of a set of nodes and a set of edges that connect pairs of nodes.
    
    A tree has the following properties:
    - One node of the tree is designated as the root node.
    - Every node n, except the root node, is connected by an edge from exactly one other node p, where p is the parent of n
    - A unique path traverses from the root to each node.
    - If each node in the tree has a maximum of two children, we say that the tree is a binary tree.


"""

def binaryTree(n):
    """
    Returns a root node with empty two lists, left subtree and right subtree
    """
    return [n,[],[]]

def insertLeft(root, newBranch):
    """
        Insert a new branch to the left of the tree
    """
    
    if len(root[1]) > 0:
        root[1] = [newBranch, root[1], []]
    else:
        root[1] = [newBranch, [], []]
    
    return root
    
def insertRight(root, newBranch):
    """
        Insert a new branch to the right of the tree
    """
    if len(root[2]) > 0:
        root[2] = [newBranch, [], root[2]]
    else:
        root[2] = [newBranch, [], []]
    
    return root
    
def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]