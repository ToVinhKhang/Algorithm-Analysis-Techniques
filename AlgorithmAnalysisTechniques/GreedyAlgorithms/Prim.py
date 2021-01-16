import time
import numpy as np
import matplotlib.pyplot as plt

class Graph(): 
    def __init__(self, nodes): 
        self.N = nodes 
        self.inputGraph = [[0 for c in range(nodes)] for r in range(nodes)]  
  
    def minIndex(self, keyPick, setNodes):   
        minValue = 99999
        for n in range(self.N): 
            if keyPick[n] < minValue and setNodes[n] == False: 
                minValue = keyPick[n] 
                index = n 
        return index 
  
    def displayResult(self, resultTree): 
        for i in range(1, self.N): 
            print(resultTree[i], i, "\t", self.inputGraph[i][resultTree[i]])

    def PrimAlgorithm(self):   
        keyPick = [99999] * self.N 
        keyPick[0] = 0 
        resultTree = [None] * self.N
        resultTree[0] = -1 
        setNodes = [False] * self.N 
        for i in range(self.N): 
            minDistanceNode = self.minIndex(keyPick, setNodes) 
            setNodes[minDistanceNode] = True
            for n in range(self.N): 
                if self.inputGraph[minDistanceNode][n] > 0 and setNodes[n] == False and keyPick[n] > self.inputGraph[minDistanceNode][n]: 
                        keyPick[n] = self.inputGraph[minDistanceNode][n] 
                        resultTree[n] = minDistanceNode 
        self.displayResult(resultTree) 
  

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
        G.PrimAlgorithm()
        T.append(time.time() - start)
        Cases.append(i)
    plt.plot(Cases, T, "-o")
    plt.xlabel('List Cases')
    plt.ylabel('List Time')
    plt.title('PrimAlgorithm') 
    plt.show()
Test()