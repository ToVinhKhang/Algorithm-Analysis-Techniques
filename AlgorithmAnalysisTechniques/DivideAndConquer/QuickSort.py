import numpy as np
import matplotlib.pyplot as plt
import time

def Partition(A, low, high):
	pivot = A[high]
	i = low - 1

	for j in range(low, high):
		if A[j] <= pivot:
			i = i + 1
			A[i], A[j] = A[j], A[i]

	A[i + 1], A[high] = A[high], A[i + 1]

	return i + 1

def QuickSort(A, low, high):
	if (len(A) == 1):
		return A

	if low < high:
		part = Partition(A, low, high)

		QuickSort(A, low, part - 1)
		QuickSort(A, part + 1, high)

		return A

def Test():
	A = np.random.randint(1000, size = 100)
	T = []

	for i in A:
		start = time.time()
		QuickSort(A, 0, len(A) - 1)
		T.append(time.time() - start)

	plt.plot(A, T, "-o")
	plt.xlabel('List A')
	plt.ylabel('List Time')
	plt.title('Quick Sort') 
	plt.show()

Test()