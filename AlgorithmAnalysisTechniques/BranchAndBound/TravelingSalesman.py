import math
import time
import matplotlib.pyplot as plt

infinity = 99999999999999999

def copySolutionToFinal(currentPath): 
    finalPath[:N + 1] = currentPath[:] 
    finalPath[N] = currentPath[0] 

def findMinimumEdgeCost(adjacencyMatrix, i): 
    minCost = infinity 

    for j in range(N): 
        if adjacencyMatrix[i][j] < minCost and i != j: 
            minCost = adjacencyMatrix[i][j] 

    return minCost

def findSecondMinimumEdgeCost(adjacencyMatrix, i): 
    firstCost, secondCost = infinity, infinity 

    for j in range(N): 
        if i == j: 
            continue

        if adjacencyMatrix[i][j] <= firstCost: 
            secondCost = firstCost 
            firstCost = adjacencyMatrix[i][j] 

        elif(adjacencyMatrix[i][j] != firstCost and adjacencyMatrix[i][j] <= secondCost): 
            secondCost = adjacencyMatrix[i][j] 

    return secondCost 
  
def SolveTravelingSalesManProblem(currentPath, currentBound, currentWeight, adjacencyMatrix, level, visited):
    global finalResult

    if level == N: 
        if adjacencyMatrix[currentPath[level - 1]][currentPath[0]] != 0: 
            currentResult = currentWeight + adjacencyMatrix[currentPath[level - 1]][currentPath[0]] 
            if currentResult < finalResult: 
                copySolutionToFinal(currentPath) 
                finalResult = currentResult 

        return

    for i in range(N): 
        if (adjacencyMatrix[currentPath[level-1]][i] != 0 and visited[i] == False): 
            temp = currentBound 
            currentWeight += adjacencyMatrix[currentPath[level - 1]][i] 
            if level == 1: 
                currentBound -= ((findMinimumEdgeCost(adjacencyMatrix, currentPath[level - 1]) + findMinimumEdgeCost(adjacencyMatrix, i)) / 2) 
            else: 
                currentBound -= ((findSecondMinimumEdgeCost(adjacencyMatrix, currentPath[level - 1]) +findMinimumEdgeCost(adjacencyMatrix, i)) / 2) 
            if currentBound + currentWeight < finalResult: 
                currentPath[level] = i 
                visited[i] = True
                SolveTravelingSalesManProblem(currentPath, currentBound, currentWeight, adjacencyMatrix, level + 1, visited) 
            currentWeight -= adjacencyMatrix[currentPath[level - 1]][i] 
            currentBound = temp 
            visited = [False] * len(visited) 
            for j in range(level): 
                if currentPath[j] != -1: 
                    visited[currentPath[j]] = True
  
def TravelingSalesmanProblem(adjacencyMatrix): 
    currentPath = [-1] * (N + 1) 
    visited = [False] * N
    currentBound = 0 
    for i in range(N): 
        currentBound += (findMinimumEdgeCost(adjacencyMatrix, i) + findSecondMinimumEdgeCost(adjacencyMatrix, i)) 
    currentBound = math.ceil(currentBound / 2) 
    visited[0] = True
    currentPath[0] = 0
    SolveTravelingSalesManProblem(currentPath, currentBound, 0, adjacencyMatrix, 1, visited)
    print("Path Taken : ", end = ' ')
    for i in range(N + 1): 
        print(finalPath[i], end = ' ')
    print()

adjacencyMatrix = [
    [0, 5, 7, 2, 10], 
    [5, 0, 14, 3, 13], 
    [7, 14, 0, 21, 6], 
    [2, 3, 21, 0, 1],
    [10, 13, 6, 1, 0]
] 
N = 5
finalPath = [None] * (N + 1) 
visited = [False] * N  
finalResult = infinity 

# import timeit
# start = timeit.default_timer()
# TravelingSalesmanProblem(adjacencyMatrix)
# end = timeit.default_timer()
# res = end - start
# print("Thời gian chạy thuật toán Traveling Salesman:", res)

def Test():
    T=[]
    Cases=[]
    for i in range(1,101):
        start=time.time()
        TravelingSalesmanProblem(adjacencyMatrix)
        T.append(time.time()-start)
        Cases.append(i)
    plt.plot(Cases, T,"-o")
    plt.xlabel('List Cases')
    plt.ylabel('List Time')
    plt.title('TravelingSalesman') 
    plt.show()
Test()
