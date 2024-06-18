t = int(input().strip())


def travel():
	n, m = map(int, input().split())

	# matrix = [[] for _ in range(m + 1)]
	# for _ in range(m):
	# 	a, b = map(int, input().split())
	# 	matrix.insert(a, b)

	# matrix = [[0] * (n + 1) for _ in range(n + 1)]
	for _ in range(m):
		a, b = map(int, input().split())
	# 	matrix[a][b] = 1
	# 	matrix[b][a] = 1
	# print(*matrix, sep='\n')
	print(n - 1)


for _ in range(t):
	travel()

# import sys
#
# input = sys.stdin.readline
#
# # Read number of test cases
# T = int(input().strip())
#
# for _ in range(T):
# 	# Read number of countries (N) and number of flights (M)
# 	N, M = map(int, input().strip().split())
#
# 	# Read M lines of flight routes (a, b)
# 	for _ in range(M):
# 		input().strip()
#
# 	# The result for each test case is always N - 1
# 	print(N - 1)
