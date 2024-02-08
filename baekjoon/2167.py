import sys

input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

# print(matrix)


K = int(input())

arr = [list(map(int, input().split())) for _ in range(K)]

# for i in range(N):
# 	print(*matrix[i])
# print(arr)

# for i in range(K):
# 	i, j, x, y = arr[i]
# 	total = 0
# 	for k in range(i-1, x):
# 		total += sum(matrix[k][j-1:y])
# 		# print(total)
# 	print(total)

# 누적 합 배열 계산
prefix_sum = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        prefix_sum[i][j] = matrix[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

# 쿼리 처리
for i, j, x, y in arr:
    result = prefix_sum[x][y] - prefix_sum[i-1][y] - prefix_sum[x][j-1] + prefix_sum[i-1][j-1]
    print(result)

