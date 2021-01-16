from collections import defaultdict
import time
import numpy as np
import matplotlib.pyplot as plt
class Graph():
    def __init__(self, nodes):
        self.N = nodes
        self.inputGraph = []
 
    def Edge(self, v1, v2, weight):
        self.inputGraph.append([v1, v2, weight])
 
    def findSetOfElement(self, parent, element):
        if parent[element] == element:
            return element

        return self.findSetOfElement(parent, parent[element])
 
    def Union(self, parent, degree, x, y):
        xRoot = self.findSetOfElement(parent, x)
        yRoot = self.findSetOfElement(parent, y)
 
        if degree[xRoot] < degree[yRoot]:
            parent[xRoot] = yRoot
            
        elif degree[xRoot] > degree[yRoot]:
            parent[yRoot] = xRoot
 
        else:
            parent[yRoot] = xRoot
            degree[xRoot] += 1
 
    def KruskalAlgorithm(self):
        result = []
        parent = []
        degree = []
        element = 0
        index = 0
        self.inputGraph = sorted(self.inputGraph, key = lambda item: item[2])
 
        for node in range(self.N):
            parent.append(node)
            degree.append(0)
 
        while index < self.N - 1:
            v1, v2, weight = self.inputGraph[element]
            element = element + 1
            x = self.findSetOfElement(parent, v1)
            y = self.findSetOfElement(parent, v2)
 
            if x != y:
                index = index + 1
                result.append([v1, v2, weight])
                self.Union(parent, degree, x, y)
 
        lowestCost = 0

        print("Cạnh \tTrọng số")

        for v1, v2, weight in result:
            lowestCost += weight

            print("%d %d \t %d" % (v1, v2, weight))

        print("--> Giá trị của cây bao trùm nhỏ nhất =", lowestCost)

def Test():
    T = []
    Cases = []
    for i in range(1,101):
        G = Graph(6)
        G.Edge(0, 1, 2)
        G.Edge(2, 3, 1)
        G.Edge(3, 5, 2)
        G.Edge(1, 5, 1)
        G.Edge(4, 0, 2)
        start = time.time()
        G.KruskalAlgorithm()
        T.append(time.time() - start)
        Cases.append(i)
    plt.plot(Cases, T, "-o")
    plt.xlabel('List Cases')
    plt.ylabel('List Time')
    plt.title('KruskalAlgorithm') 
    plt.show()
Test()