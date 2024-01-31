import sys
sys.setrecursionlimit(10**6)

S = int(input())


def add(total, n, s):
	total = total + n
	if total > s:
		return n - 1
	return add(total, n + 1, s)


print(add(0, 1, S))

# S = int(input())
# n = 0
# total = 0
#
# while total <= S:
#     n += 1
#     total += n
#
# print(n - 1)
