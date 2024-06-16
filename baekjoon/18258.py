import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())

queue = deque([])

for _ in range(n):
    order = input().strip()
    if order.startswith('push'):
        _, num = order.split()
        queue.append(int(num))
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif order == 'pop':
        print(queue.popleft() if len(queue) > 0 else -1)
    elif order == 'front':
        print(queue[0] if len(queue) > 0 else -1)
    elif order == 'back':
        print(queue[-1] if len(queue) > 0 else -1)
