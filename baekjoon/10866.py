from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

arr = deque()

# print(arr)

for _ in range(N):
	order = input().strip()
	# print(order)
	length = len(arr)
	if 'push_front' in order:
		order2, num = map(str, order.split())
		arr.appendleft(int(num))
	elif 'push_back' in order:
		order2, num = map(str, order.split())
		arr.append(int(num))
	elif order == 'pop_front':
		if length == 0:
			print(-1)
		else:
			print(arr.popleft())
	elif order == 'pop_back':
		if length == 0:
			print(-1)
		else:
			print(arr.pop())
	elif order == 'size':
		print(length)
	elif order == 'empty':
		if length == 0:
			print(1)
		else:
			print(0)
	elif order == 'front':
		if length == 0:
			print(-1)
		else:
			print(arr[0])
	elif order == 'back':
		if length == 0:
			print(-1)
		else:
			print(arr[-1])


# from collections import deque
# import sys
#
# input = sys.stdin.readline
# N = int(input())
#
# arr = deque()
#
#
# for _ in range(N):
#   order = input().strip()  # 개행 문자 제거
#   if 'push_front' in order:
#       _, num = order.split()
#       arr.appendleft(int(num))
#   elif 'push_back' in order:
#       _, num = order.split()
#       arr.append(int(num))
#   elif order == 'pop_front':
#       if not arr:
#           print(-1)
#       else:
#           print(arr.popleft())
#   elif order == 'pop_back':
#       if not arr:
#           print(-1)
#       else:
#           print(arr.pop())
#   elif order == 'size':
#       print(len(arr))
#   elif order == 'empty':
#       print(1 if not arr else 0)
#   elif order == 'front':
#       print(arr[0] if arr else -1)
#   elif order == 'back':
#       print(arr[-1] if arr else -1)
