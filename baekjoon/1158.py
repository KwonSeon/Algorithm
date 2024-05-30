from collections import deque

n, k = map(int, input().split())

q = deque([i for i in range(1, n + 1)])
ans = []

while q:
	for i in range(k - 1):
		num = q.popleft()
		q.append(num)
	ans.append(str(q.popleft()))


result = ', '.join(ans)
print(f'<{result}>')