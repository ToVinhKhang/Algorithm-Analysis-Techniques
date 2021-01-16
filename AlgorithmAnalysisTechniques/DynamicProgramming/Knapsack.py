import time
import matplotlib.pyplot as plt
import numpy as np
import random
def Knapsack(C, W, V, n): 
	F = [[0 for x in range(C + 1)] for x in range(n + 1)] 
	for i in range(n + 1): 
		for c in range(C + 1): 
			if W[i-1] <= c: 
				F[i][c] = max(V[i-1] + F[i-1][c-W[i-1]], F[i-1][c]) 
			else: 
				F[i][c] = F[i-1][c] 

	return F[n][C]

# import timeit
# C = 50
# W = [10, 30, 40]
# V = [20, 50, 110]
# n = len(V)
# print("Giá trị có được khi xếp vào túi có sức chứa", C)
# start = timeit.default_timer()
# print(Knapsack(C, W, V, n))
# end = timeit.default_timer()
# res = end - start
# print("Thời gian chạy thuật toán Change-Making:", res)

def Test():
	W = np.random.randint(1000, size = (100, 100))
	V = np.random.randint(1000, size = (100, 100))
	A=[]
	T=[]
	for i in range(100):
		C = random.randint(100 ,1000)
		A.append(C)
		start=time.time()
		Knapsack(C, W[i], V[i], len(V))
		T.append(time.time()-start)
	plt.plot(A, T,"-o")
	plt.xlabel('List Capacity')
	plt.ylabel('List Time')
	plt.title('Knapsack') 
	plt.show()
Test()