import time
import matplotlib.pyplot as plt
import random
def fibonacci(n):  
	FibArray = [0, 1]  
	while len(FibArray) < n + 1:  
		FibArray.append(0)   
	for i in range(2, n+1):
		FibArray[i] = FibArray[i - 2] + FibArray[i - 1]  
	return FibArray

# import timeit
# n = 10
# print("Dãy Fibonacci từ 0 đến", n, "là:")
# start = timeit.default_timer()
# print(fibonacci(n))
# end = timeit.default_timer()
# res = end - start
# print("Thời gian chạy thuật toán Fibonacci:", res)


def Test():
	A = []
	for i in range(100):
		A.append(random.randint(0, 1000))
	T=[]
	for i in A:
		start=time.time()
		print(fibonacci(i))
		T.append(time.time()-start)
	plt.plot(A,T,"-o")
	plt.xlabel('List A')
	plt.ylabel('List Time')
	plt.title('Fibonacci') 
	plt.show()
Test()