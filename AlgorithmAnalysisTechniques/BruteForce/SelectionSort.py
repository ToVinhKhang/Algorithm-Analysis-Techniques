import numpy as np
import matplotlib.pyplot as plt
import time

def SelectionSort(A):
	N=len(A)
	for i in range(N):
		MIN = i 
		for j in range(i+1,N): 
			if(A[MIN] > A[j]):
				MIN = j         
		A[i], A[MIN] = A[MIN], A[i]
	return A 
def Test():
	A=np.random.randint(1000, size=100)
	T=[]
	for i in A:
		start=time.time()
		SelectionSort(A)
		T.append(time.time()-start)
	plt.plot(A,T,"-o")
	plt.xlabel('List A')
	plt.ylabel('List Time')
	plt.title('SelectionSort') 
	plt.show()
Test()

