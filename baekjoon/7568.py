N = int(input())
body = []

for _ in range(N):
	x, y = map(int,input().split())
	body.append((x, y))

# print(body)

ans = [1] * N

for i in range(N-1):
	for j in range(i+1, N):
		if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
			ans[i] += 1
		elif body[i][0] > body[j][0] and body[i][1] > body[j][1]:
			ans[j] += 1

# for i in range(N):
# 	for j in range(N):
# 		if i == j:
# 			pass
# 		elif body[i][0] < body[j][0] and body[i][1] < body[j][1]:
# 			ans[i] += 1
# 		elif body[i][0] < body[j][0] and body[i][1] < body[j][1]:
# 			ans[j] += 1

print(*ans)