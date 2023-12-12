import sys
sys.setrecursionlimit(10**6)

n = int(input())

dp = [-1] * 1001
dp[1] = 1
dp[2] = 2


def tile(n):
	if dp[n] == -1:
		dp[n] = (tile(n - 1) + tile(n - 2)) % 10007
	return dp[n]


print(tile(n))