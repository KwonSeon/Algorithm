N = int(input())

dp = [[-1] * 10 for _ in range(N + 1)]
dp[1] = [0] + [1] * 9


# print(dp[1])
# print(dp)
# print(len(dp[2]))


def stair(n):
	if n == 1:
		return sum(dp[n]) % 10 ** 9
	if dp[n - 1][0] == -1:
		stair(n - 1)
	for i in range(10):
		if i == 0:
			dp[n][i] = dp[n - 1][i + 1]
		elif i == 9:
			dp[n][i] = dp[n - 1][i - 1]
		else:
			dp[n][i] = dp[n - 1][i - 1] + dp[n - 1][i + 1]
	# print(dp[n])
	return sum(dp[n]) % 10 ** 9


print(stair(N))

# 아래부터는 최적화 코드
# Top-Down
# N = int(input())
#
# # 메모이제이션을 위한 dp 배열 초기화
# dp = [[-1 for _ in range(10)] for _ in range(N + 1)]
#
#
# def stair(n, last_digit):
# 	if n == 1:
# 		return 0 if last_digit == 0 else 1
# 	if dp[n][last_digit] != -1:
# 		return dp[n][last_digit]
#
# 	dp[n][last_digit] = 0
# 	if last_digit > 0:
# 		dp[n][last_digit] += stair(n - 1, last_digit - 1)
# 	if last_digit < 9:
# 		dp[n][last_digit] += stair(n - 1, last_digit + 1)
# 	dp[n][last_digit] %= 10 ** 9
# 	return dp[n][last_digit]
#
#
# # 모든 1부터 9까지의 마지막 숫자에 대해 계산
# result = sum(stair(N, i) for i in range(10)) % 10 ** 9
# print(result)

# Bottom-Up
# N = int(input())
#
# dp = [[0] * 10 for _ in range(N + 1)]
# dp[1] = [0] + [1] * 9
#
# for n in range(2, N + 1):
#     for i in range(10):
#         if i == 0:
#             dp[n][i] = dp[n - 1][i + 1]
#         elif i == 9:
#             dp[n][i] = dp[n - 1][i - 1]
#         else:
#             dp[n][i] = dp[n - 1][i - 1] + dp[n - 1][i + 1]
#         dp[n][i] %= 10**9
#
# print(sum(dp[N]) % 10**9)
