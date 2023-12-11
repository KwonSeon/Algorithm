import sys

sys.setrecursionlimit(10 ** 6)

MOD = 10007
N, K = map(int, input().split())
# print(N, K)
dp = [[-1] * (K + 1) for _ in range(N + 1)]


for i in range(N + 1):
	for j in range(min(i, K) + 1):
		if j == 0 or i == j:
			dp[i][j] = 1
		else:
			dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD

# for i in range(10):
# 	print(dp[i])

print(dp[N][K])

# def binom(n, k):
# 	if dp[n][k] != -1:
# 		return dp[n][k]
#
# 	if k == 0 or k == n:
# 		dp[n][k] = 1
# 	else:
# 		dp[n][k] = (binom(n - 1, k - 1) + binom(n - 1, k)) % MOD
# 	return dp[n][k]


# print(binom(N, K))
