import numpy as np
import matplotlib.pyplot as plt
import time

def SequentialSearch(A,key):
	i = 0
	N = len(A)
	while (i<N):
		if(A[i]==key): 
			return i
		else: 
			i+=1
	return "Notfound"
def Test():
	A=np.random.randint(1000, size=100)
	key=A[0]
	print(A)
	print(key)
	T=[]
	for i in A:
		start=time.time()
		print(SequentialSearch(A,key))
		T.append(time.time()-start)
	plt.plot(A,T,"-o")
	plt.xlabel('List A')
	plt.ylabel('List Time')
	plt.title('SequentialSearch') 
	plt.show()
Test()
