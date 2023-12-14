M, N = map(int, input().split())

board = [input() for _ in range(M)]

# print(M, N)
# for i in range(len(board)):
# 	print(board[i])

ans = 65


# def chess(M, N):
# 	a = 0
# 	b = 0
# 	for i in range(8):
# 		for j in range(8):
# 			if (i + j) % 2 == 0:
# 				if board[M + i][N + j] != 'W':
# 					a += 1
# 				elif board[M + i][N + j] != 'B':
# 					b += 1
# 			else:
# 				if board[M + i][N + j] != 'B':
# 					a += 1
# 				else:
# 					b += 1
# 		# print(f'board[{M+i}][{N+j}]')
# 	# print(f'a:{a}, b:{b}')
# 	return min(a, b)
#
#
# for i in range(M - 7):
# 	for j in range(N - 7):
# 		# print(f'board[{i}][{j}]')
# 		# print('chess', chess(i, j))
# 		if chess(i, j) < ans:
# 			ans = chess(i, j)
#
# print(ans)

def fill(y, x, bw):
	global ans
	cnt = 0
	for i in range(8):
		for j in range(8):
			if (i + j) % 2:
				if board[y + i][x + j] == bw:
					cnt += 1
			else:
				if board[y + i][x + j] != bw:
					cnt += 1
	ans = min(cnt, ans)


for i in range(M - 7):
	for j in range(N - 7):
		fill(i, j, 'B')
		fill(i, j, 'W')

print(ans)