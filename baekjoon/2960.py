from collections import deque

N, K = map(int, input().split())

arr = deque([i for i in range(2, N + 1)])

# print(arr)

cnt = 0

while cnt < K:
	num = arr[0]
	i = 1
	while num * i <= arr[-1]:
		if num * i in arr:
			cnt += 1
			arr.remove(num * i)
		if cnt == K:
			print(num * i)
			break
		i += 1


# N, K = map(int, input().split())
#
# # N+1 크기의 리스트를 생성하고 모든 값을 True로 초기화한다.
# # 이때, prime_check[0]과 prime_check[1]은 사용하지 않을 것이다.
# prime_check = [True] * (N + 1)
# count = 0
#
# for i in range(2, N + 1):
#     if prime_check[i]:  # i가 소수인 경우
#         for j in range(i, N+1, i):
#             if prime_check[j]:  # 아직 지워지지 않은 경우
#                 prime_check[j] = False  # 소수의 배수를 지운다
#                 count += 1
#                 if count == K:
#                     print(j)
#                     break