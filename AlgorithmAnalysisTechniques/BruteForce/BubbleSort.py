import numpy as np
import matplotlib.pyplot as plt
import time

def BubbleSort(A):
	N = len(A)
	for i in range(N-1):
		for j in range(N-1):
			if(A[j] > A[j+1]):
				A[j], A[j+1] = A[j+1], A[j]
	return A
def Test():
	A=np.random.randint(1000, size=100)
	T=[]
	for i in A:
		start=time.time()
		BubbleSort(A)
		T.append(time.time()-start)
	plt.plot(A,T,"-o")
	plt.xlabel('List A')
	plt.ylabel('List Time')
	plt.title('BubbleSort') 
	plt.show()
Test()
