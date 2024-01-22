from queue import PriorityQueue

N = int(input())

q = PriorityQueue()

for _ in range(N):
	x, y = map(int, input().split())
	q.put((x, y))

for _ in range(N):
	print(*q.get())