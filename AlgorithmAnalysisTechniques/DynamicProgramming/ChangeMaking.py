import time
import matplotlib.pyplot as plt
import numpy as np
import random
def ChangeMaking(d, S, coins, used):
	for s in range(S + 1):
		count = s
		newCoin = 1
		for j in [c for c in d if c <= s]:
			if coins[s-j] + 1 < count:
				count = coins[s-j] + 1
				newCoin = j
		coins[s] = count
		used[s] = newCoin
	return coins

# import timeit
# d = [1, 2, 5, 10]
# S = 57
# coins = [0]*(S + 1)
# used = [0]*(S + 1)
# print("Bảng quy đổi coins của giá trị", S)
# start = timeit.default_timer()
# print(ChangeMaking(d, S, coins, used))
# end = timeit.default_timer()
# res = end - start
# print("Thời gian chạy thuật toán Change-Making:", res)


def Test():
	d=[1, 2, 5, 10, 20, 50, 100]
	A=[]
	T=[]
	for i in range(100):
		S = random.randint(100 ,10000)
		A.append(S)
		coins= [0]*(S + 1)
		used = [0]*(S + 1)
		start=time.time()
		ChangeMaking(d, S, coins, used)
		T.append(time.time()-start)
	plt.plot(A, T,"-o")
	plt.xlabel('List Change Amount')
	plt.ylabel('List Time')
	plt.title('ChangeMaking') 
	plt.show()
Test()