N, M = map(int, input().split())

friends = [[float('inf')] * (N) for _ in range(N)]

for _ in range(M):
	A, B = map(int, input().split())
	friends[A-1][B-1] = 1
	friends[B-1][A-1] = 1

for i in range(N):
	friends[i][i] = 0

# for i in range(N):
# 	print(friends[i])

for k in range(N):
	for i in range(N):
		for j in range(N):
			friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])
			# print(f'k: {k}, i: {i}, j: {j}')
			# for l in range(N):
			# 	print(friends[l])

min_friends = [sum(friends[i]) for i in range(N)]

print(min_friends.index(min(min_friends)) + 1)

# from collections import deque
#
#
# def bfs(N, friends, start):
#     distances = [float('inf')] * N
#     distances[start] = 0
#     queue = deque([start])
#
#     while queue:
#         current = queue.popleft()
#         for i in range(N):
#             if friends[current][i] == 1 and distances[i] == float('inf'):
#                 distances[i] = distances[current] + 1
#                 queue.append(i)
#     return distances
#
#
# N, M = map(int, input().split())
#
# friends = [[0] * N for _ in range(N)]
#
# for _ in range(M):
#     A, B = map(int, input().split())
#     friends[A-1][B-1] = 1
#     friends[B-1][A-1] = 1
#
# kevin_bacon_numbers = [0] * N
# for i in range(N):
#     distances = bfs(N, friends, i)
#     kevin_bacon_numbers[i] = sum(distances)
#
# print(kevin_bacon_numbers.index(min(kevin_bacon_numbers)) + 1)

