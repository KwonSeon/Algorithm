t = int(input().strip())


def fibonacci(n):
	if n == 0:
		count_zero.append(1)
		return 0
	elif n == 1:
		count_one.append(1)
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)


for _ in range(t):
	n = int(input().strip())
	count_zero = []
	count_one = []
	fibonacci(n)
	print(f'{sum(count_zero)} {sum(count_one)}')


# def fibonacci_counts(n):
# 	counts = [(1, 0), (0, 1)]  # (count of 0s, count of 1s) for fib(0) and fib(1)
#
# 	for i in range(2, n + 1):
# 		count_zero = counts[i - 1][0] + counts[i - 2][0]
# 		count_one = counts[i - 1][1] + counts[i - 2][1]
# 		counts.append((count_zero, count_one))
#
# 	return counts
#
#
# T = int(input())
# cases = [int(input()) for _ in range(T)]
#
# counts = fibonacci_counts(max(cases))
#
# for case in cases:
# 	print(counts[case][0], counts[case][1])