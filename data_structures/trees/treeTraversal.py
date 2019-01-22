# Traversing the Binary tree

import sys
import os
import unittest

class TheBinaryTree:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preOrder(rootNode, nodes):
    """
        1. Visit the root
        2. Traverse the left subtree, i.e., call Preorder(left-subtree)
        3. Traverse the right subtree, i.e., call Preorder(right-subtree) 
    """
    nodes.append(rootNode.data)
    if rootNode.leftChild:
        preOrder(rootNode.leftChild, nodes)
    if rootNode.rightChild:
        preOrder(rootNode.rightChild, nodes)
    return nodes
    
def postOrder(rootNode, nodes):
    """
        1. Traverse the left subtree, i.e., call Postorder(left-subtree)
        2. Traverse the right subtree, i.e., call Postorder(right-subtree)
        3. Visit the root
    """
    if rootNode.leftChild:
        postOrder(rootNode.leftChild,nodes)
    if rootNode.rightChild:
        postOrder(rootNode.rightChild,nodes)
    nodes.append(rootNode.data)
    return nodes
    
def inOrder(rootNode, nodes):
    """
        1. Traverse the left subtree, i.e., call Inorder(left-subtree)
        2. Visit the root
        3. Traverse the right subtree, i.e., call Inorder(right-subtree)
    """
    if rootNode.leftChild:
        inOrder(rootNode.leftChild,nodes)
    nodes.append(rootNode.data)
    if rootNode.rightChild:
        inOrder(rootNode.rightChild,nodes)
    return nodes

def levelOrder(rootNode, nodes):
    """
        1) Add the root to a queue.
        2) Pop the last node from the queue, and return its value.
        3) Add all children of popped node to queue, and continue from step 2 until queue is empty.
    """
    queue = [rootNode]
    while(queue):
        temp = queue.pop(0)
        nodes.append(temp.data)
        if temp.leftChild:
            queue.append(temp.leftChild)
        if temp.rightChild:
            queue.append(temp.rightChild)
    return nodes

class treeTraversalTest(unittest.TestCase):
    def setUp(self):
        self.rootN = TheBinaryTree('A')
        self.n1 = TheBinaryTree('B')
        self.n2 = TheBinaryTree('C')
        self.n3 = TheBinaryTree('D')
        self.n4 = TheBinaryTree('E')

        # Setup children
        self.rootN.leftChild = self.n1
        self.rootN.rightChild = self.n2
        self.n1.leftChild = self.n3
        self.n1.rightChild = self.n4

    def testPreOrder(self):
        self.assertListEqual(preOrder(self.rootN,[]),['A', 'B', 'D', 'E', 'C'])

    def testPostOrder(self):
        self.assertListEqual(postOrder(self.rootN,[]),['D', 'E', 'B', 'C', 'A'])

    def testInOrder(self):
        self.assertListEqual(inOrder(self.rootN,[]),['D', 'B', 'E', 'A', 'C'])

    def testLevelOrder(self):
        self.assertListEqual(levelOrder(self.rootN,[]),['A', 'B', 'C', 'D', 'E'])

if __name__ == "__main__":
    unittest.main()
