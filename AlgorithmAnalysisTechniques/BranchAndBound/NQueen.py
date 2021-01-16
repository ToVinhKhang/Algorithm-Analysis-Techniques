import time
import matplotlib.pyplot as plt

def checkToPlaceQueen(slashCode, backslashCode, row, col, rowCheck, slashCodeCheck, backslashCheck):
	if (rowCheck[row] or slashCodeCheck[slashCode[row][col]] or backslashCheck[backslashCode[row][col]]):
		return False

	return True

def solveNQueensProblem(chessboard, col, slashCode, backslashCode, rowCheck, slashCodeCheck, backslashCheck):                
	if(col >= N):
		return True

	for i in range(N):
		if(checkToPlaceQueen(slashCode, backslashCode, i, col, rowCheck, slashCodeCheck, backslashCheck)):
			slashCodeCheck[slashCode[i][col]] = True
			backslashCheck[backslashCode[i][col]] = True
			chessboard[i][col] = 1
			rowCheck[i] = True

			if(solveNQueensProblem(chessboard, col + 1, slashCode, backslashCode, rowCheck, slashCodeCheck, backslashCheck)):
				return True

			slashCodeCheck[slashCode[i][col]] = False
			backslashCheck[backslashCode[i][col]] = False
			chessboard[i][col] = 0
			rowCheck[i] = False

	return False
 
def NQueensProblem_BrandAndBound():
	chessboard = [[0 for i in range(N)] for j in range(N)]
	slashCode = [[0 for i in range(N)] for j in range(N)]
	backslashCode = [[0 for i in range(N)] for j in range(N)]
	rowCheck = [False] * N
	slashCodeCheck = [False] * (2 * N - 1)
	backslashCheck = [False] * (2 * N - 1)
	for rs in range(N):
		for cs in range(N):
			slashCode[rs][cs] = rs + cs
			backslashCode[rs][cs] = rs - cs + 7
	if(solveNQueensProblem(chessboard, 0, slashCode, backslashCode, rowCheck, slashCodeCheck, backslashCheck) == False):
		print("Can't solve")
		return False
	for i in range(N):
		for j in range(N):
			print(chessboard[i][j], end = " ")
		print()
	return True

# N = 8
# import timeit
# print("N Queen solution with N = ", N)
# start = timeit.default_timer()
# NQueensProblem_BrandAndBound()
# end = timeit.default_timer()
# res = end - start
# print("Thời gian chạy thuật toán N Queen Problem:", res)

N = 8
def Test():
	T=[]
	Cases=[]
	for i in range(1,101):
		start=time.time()
		NQueensProblem_BrandAndBound()
		T.append(time.time()-start)
		Cases.append(i)
	plt.plot(Cases, T,"-o")
	plt.xlabel('List Cases')
	plt.ylabel('List Time')
	plt.title('N Queen') 
	plt.show()
Test()

