from collections import deque as dq

N = int(input())

order_list = dq([input().strip() for _ in range(N)])
arr = dq([])


while order_list:
	order = str(order_list.popleft())
	# print(order)
	if 'push' in order:
		o, c = map(str, order.split())
		c = int(c)
		arr.append(c)
	elif order == 'pop':
		if len(arr) < 1:
			print(-1)
		else:
			print(arr.popleft())
	elif order == 'size':
		print(len(arr))
	elif order == 'empty':
		if len(arr) < 1:
			print(1)
		else:
			print(0)
	elif order == 'front':
		if len(arr) < 1:
			print(-1)
		else:
			print(arr[0])
	elif order == 'back':
		if len(arr) < 1:
			print(-1)
		else:
			print(arr[-1])

# import sys
#
# input = sys.stdin.readline
# N = int(input())
#
# queue = []
# result = []
#
# for _ in range(N):
#     command = input().split()
#     print('command', command)
#     if command[0] == 'push':
#         queue.append(int(command[1]))
#     elif command[0] == 'pop':
#         result.append(str(queue.pop(0) if queue else -1))
#     elif command[0] == 'size':
#         result.append(str(len(queue)))
#     elif command[0] == 'empty':
#         result.append('0' if queue else '1')
#     elif command[0] == 'front':
#         result.append(str(queue[0] if queue else -1))
#     elif command[0] == 'back':
#         result.append(str(queue[-1] if queue else -1))
#
# print('\n'.join(result))
