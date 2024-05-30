import sys

input = sys.stdin.readline

n = int(input().rstrip())

array = list(map(int, input().split()))
array.sort(reverse=True)

dp = [0] * n

m = 0
while array:
	dp[m] = dp[m - 1] + array.pop()
	m += 1

print(sum(dp))