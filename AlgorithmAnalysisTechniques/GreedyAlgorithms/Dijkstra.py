import time
import numpy as np
import matplotlib.pyplot as plt
class Graph(): 
    def __init__(self, nodes): 
        self.N = nodes 
        self.inputGraph = [[0 for c in range(nodes)] for r in range(nodes)] 
   
    def minDistanceValue(self, result, shortestPathSet):    
        minDistance = 99999 
        for n in range(self.N): 
            if result[n] < minDistance and shortestPathSet[n] == False: 
                minDistance = result[n] 
                minIndex = n 
        return minIndex 

    def displayResult(self, result): 
        for node in range(self.N): 
            print (node, "\t", result[node]) 
   
    def DijkstraAlgorithm(self, source): 
        result = [99999] * self.N 
        result[source] = 0
        shortestPathSet = [False] * self.N 
        for i in range(self.N): 
            pickMinDistance = self.minDistanceValue(result, shortestPathSet) 
            shortestPathSet[pickMinDistance] = True

            for n in range(self.N): 
                if self.inputGraph[pickMinDistance][n] > 0 and shortestPathSet[n] == False and result[n] > result[pickMinDistance] + self.inputGraph[pickMinDistance][n]: 
                    result[n] = result[pickMinDistance] + self.inputGraph[pickMinDistance][n] 
        self.displayResult(result) 
   
def Test():
    T = []
    Cases = []
    for i in range(1,101):
        A = np.random.randint(0,10,6)
        B = np.random.randint(0,10,6)
        C = np.random.randint(0,10,6)
        D = np.random.randint(0,10,6)
        E = np.random.randint(0,10,6)
        F = np.random.randint(0,10,6)
        G = Graph(6) 
        G.inputGraph = [A,B,C,D,E,F]
        start = time.time()
        G.DijkstraAlgorithm(0)
        T.append(time.time() - start)
        Cases.append(i)
    plt.plot(Cases, T, "-o")
    plt.xlabel('List Cases')
    plt.ylabel('List Time')
    plt.title('DijkstraAlgorithm') 
    plt.show()
Test()