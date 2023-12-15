import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, P = map(int, input().split())

matrix = [[] for _ in range(N + 1)]
cnt = 0

for i in range(N):
	n, p = map(int, input().split())
	position = bisect_left(matrix[n], p)

	if len(matrix[n]) == position:
		matrix[n].append(p)
		cnt += 1
	else:
		while matrix[n] and matrix[n][-1] > p:
			matrix[n].pop()
			cnt += 1
		if not matrix[n] or matrix[n][-1] < p:
			matrix[n].append(p)
			cnt += 1
print(cnt)
