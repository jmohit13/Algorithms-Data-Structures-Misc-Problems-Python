import sys
import os
import unittest

class Vertex:
    """
         Represent the vertex in the graph. 
         Each vertex has a key and dictionary having information of connected vertices
    """
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.dist = sys.maxsize
        self.color = 'white'
        self.pred = None # predecessor
        
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    def setDistance(self,d):
        self.dist = d
        
    def setColor(self,color):
        self.color = color
        
    def setPred(self,p):
        self.pred = p
        
    def getDistance(self):
        return self.dist
    
    def getColor(self):
        return self.color
    
    def getPred(self):
        return self.pred

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
        
    def getConnections(self):
        """
            Returns all the vertices in adjacency list as represented by connectedTo variable
        """
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
class Graph:
    """
        This holds the master list of vertices
    """
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        
    def addVertex(self, key):
        self.numVertices += 1
        temp_vertex = Vertex(key)
        self.vertList[key] = temp_vertex
        return temp_vertex
    
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            temp_vertex = self.addVertex(f)
        if t not in self.vertList:
            temp_vertex = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    

class adjGraphTest(unittest.TestCase):
    def setUp(self):
        self.tempGraph = Graph()

    def testMakeGraph(self):
        l = [(0,1),(0,2),(1,2),(2,3),(3,4),(3,5),(4,0)]
        for i in l:
            v1, v2 = i[0], i[1]
            self.tempGraph.addEdge(v1,v2)            
        for i in self.tempGraph:
            adj = i.getConnections()
            for k in adj:
                print(str(i.id) + ' connectedTo: ' + str([x.id for x in i.connectedTo]) + ' ' 
                    + str(k.id) + ' connectedTo: ' + str([x.id for x in k.connectedTo]))


if __name__ == "__main__":
    unittest.main()

    # g = Graph()
    # for i in range(6):
    #     g.addVertex(i)

    # print("Vertices List :",g.vertList)

    # g.addEdge(0,1,5)
    # g.addEdge(0,2,2)
    # g.addEdge(1,2,3)
    # g.addEdge(2,3,9)
    # g.addEdge(3,4,7)
    # g.addEdge(3,5,3)
    # g.addEdge(4,0,1)
    # g.addEdge(5,4,8)
    # g.addEdge(5,2,1)

    # for v in g:
    #     for w in v.getConnections():
    #         print(v.getId(), w.getId())
            
    # print("Vertices List :",g.getVertices())
    # print("Number of vertices :",g.numVertices)