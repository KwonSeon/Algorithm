N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

# print(A)
# print(B)

ans = 0
for i in range(N):
	ans += A[i] * B[i]

print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
#
# # A와 B를 각각 내림차순, 오름차순으로 정렬
# A.sort(reverse=True)
# B.sort()
#
# # S의 최솟값 계산 및 출력
# print(sum(a * b for a, b in zip(A, B)))