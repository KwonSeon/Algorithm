from collections import deque

N, K = map(int, input().split())

q = deque()

for i in range(1, N + 1):
	q.append(i)

ans = []

# print(q)

while len(q) > 0:
	for _ in range(K-1):
		q.append(q.popleft())

	ans.append(q.popleft())

# print(ans)

print(f'<{", ".join(map(str, ans))}>')

# from collections import deque
#
# def josephus_sequence(n, k):
#     q = deque(range(1, n + 1))
#     ans = []
#
#     while q:
#         q.rotate(-(k-1))
#         ans.append(q.popleft())
#
#     return f'<{", ".join(map(str, ans))}>'
#
# N, K = map(int, input().split())
# print(josephus_sequence(N, K))
