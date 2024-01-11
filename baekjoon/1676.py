# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
# N = int(input())
#
#
# def factorial(N):
# 	if N == 1:
# 		return 1
# 	return N * factorial(N - 1)
#
#
# # print(factorial(N))
#
# F = factorial(N)
#
# # print(F)
#
# def countzero(F, cnt):
# 	if F // 10 == 0:
# 		return cnt
# 	if F % 10 == 0:
# 		cnt += 1
# 		return countzero(F // 10, cnt)
# 	else:
# 		return cnt
#
#
# cnt = 0
# print(countzero(F, cnt))

N = int(input())

def count_zero(N):
    count = 0
    while N >= 5:
        N //= 5
        count += N
    return count

print(count_zero(N))
