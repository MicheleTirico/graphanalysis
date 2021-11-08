
import networkx as nx
"""
with this class, I would compute the degree distribution of a single graph
input  : a graf with networkx
output : the list of degree
"""


class Degree :
    def __init__ (self, G , id  ):
        """initilize graph with an id"""
        self.G = G
        self.id = id

    def getDistrDegreeNorm (self):
        nodeCount = len(self.G)
        listDegree = []
        listNode = []
        for v in self.G.degree():
            listNode.append(v[1])
        for i in range(0,max(listNode)+1):
            listDegree.append(listNode.count(i)/nodeCount)
        return listDegree

    def getDistrDegree (self):
        listDegree = []
        listNode = []
        for v in self.G.degree():
            listNode.append(v[1])
        for i in range(0,max(listNode)+1):
            listDegree.append(listNode.count(i))
        return listDegree
