n, m = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(n)]

# print(matrix)
# for i in range(n):
# 	print(matrix[i])

dp = [[0] * m for _ in range(n)]

max_length = 0

# print(dp)

for i in range(n):
	for j in range(m):
		# 첫 번째인 경우 매트릭스의 숫자를 따라간다
		if i == 0 or j == 0:
			dp[i][j] = matrix[i][j]
		# 1을 만나는 경우 좌, 상, 좌상의 숫자를 보고 가장 작은 수에 1을 더한다
		elif matrix[i][j] == 1:
			dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
		max_length = max(max_length, dp[i][j])

		# for k in range(n):
		# 	print(dp[k])
		# print('-'*10)

print(max_length ** 2)