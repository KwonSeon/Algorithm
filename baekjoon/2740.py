N, M = map(int, input().split())

matrixA = []
for _ in range(N):
	matrixA.append(list(map(int, input().split())))

M, K = map(int, input().split())

matrixB = []
for _ in range(M):
	matrixB.append(list(map(int, input().split())))

# for i in range(N):
# 	print(matrixA[i])
# for i in range(M):
# 	print(matrixB[i])

matrix = [[] for _ in range(N)]

for i in range(N):
	for j in range(K):
		ans = 0
		for k in range(M):
			ans += matrixA[i][k] * matrixB[k][j]
		matrix[i].append(ans)

for i in range(N):
	print(*matrix[i])


# N, M = map(int, input().split())
# matrixA = [list(map(int, input().split())) for _ in range(N)]
#
# M, K = map(int, input().split())
# matrixB = [list(map(int, input().split())) for _ in range(M)]
#
# # 결과 행렬을 0으로 초기화
# matrix = [[0] * K for _ in range(N)]
#
# # 행렬 곱셈
# for i in range(N):
#     for j in range(K):
#         for k in range(M):
#             matrix[i][j] += matrixA[i][k] * matrixB[k][j]
#
# # 결과 출력
# for row in matrix:
#     print(*row)
