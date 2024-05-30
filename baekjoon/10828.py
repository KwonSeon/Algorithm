import sys

input = sys.stdin.readline

n = int(input())


def order_stack(order, stack):
	if order == 'pop':
		if len(stack) == 0:
			print(-1)
		else:
			print(stack.pop())
	elif order == 'size':
		print(len(stack))
	elif order == 'empty':
		if len(stack) == 0:
			print(1)
		else:
			print(0)
	elif order == 'top':
		if len(stack) == 0:
			print(-1)
		else:
			print(stack[-1])
	else:
		push, x = order.split()
		stack.append(x)


ans = []
for _ in range(n):
	order = input().rstrip()
	order_stack(order, ans)