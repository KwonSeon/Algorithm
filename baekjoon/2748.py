# Top-Down
dp = [-1] * 91
dp[0] = 0
dp[1] = 1


# print(dp)

def fibonacci(n):
	# if n == 0 or n == 1:
	# 	return dp[n]
	# elif dp[n - 1] == 0 or dp[n - 2] == 0 and not n == 2:
	# 	return fibonacci(n - 1) + fibonacci(n - 2)
	# else:
	# 	dp[n] = dp[n - 1] + dp[n - 2]
	# 	return dp[n]
	if dp[n] == -1:
		dp[n] = fibonacci(n - 2) + fibonacci(n - 1)
	return dp[n]


N = int(input())

print(fibonacci(N))

# Bottom-Up
# N = int(input())
# dp = [-1] * 91
# dp[0] = 0
# dp[1] = 1
#
# for i in range(2, N+1):
# 	dp[n] = dp[n - 1] + dp[n - 2]
#
# print(dp[N])
