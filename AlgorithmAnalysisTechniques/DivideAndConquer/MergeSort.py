import numpy as np
import matplotlib.pyplot as plt
import time

def MergeSort(A):
	if len(A) > 1:
		mid = len(A) // 2

		firstPart = A[:mid]
		secondPart = A[mid:]

		MergeSort(firstPart)
		MergeSort(secondPart)

		i = 0
		j = 0
		k = 0

		while i < len(firstPart) and j < len(secondPart):
			if firstPart[i] < secondPart[j]:
				A[k] = firstPart[i]
				i = i + 1

			else:
				A[k] = secondPart[j]
				j = j + 1

			k = k + 1

		while i < len(firstPart):
			A[k] = firstPart[i]
			i = i + 1
			k = k + 1

		while j < len(secondPart):
			A[k] = secondPart[j]
			j = j + 1
			k = k + 1

def Test():
	A = np.random.randint(1000, size = 100)
	T = []

	for i in A:
		start = time.time()
		MergeSort(A)
		T.append(time.time() - start)

	plt.plot(A, T, "-o")
	plt.xlabel('List A')
	plt.ylabel('List Time')
	plt.title('Merge Sort') 
	plt.show()

Test()