import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# M개의 문자열 중에 집합 S에 포한되지 않지만 중복될 수도 있다.


def is_in(string, arr):
	if string in arr:
		return 1
	else:
		return 0


arr_S = set(input() for _ in range(N))
arr_M = [input() for _ in range(M)]

ans = sum(is_in(M, arr_S) for M in arr_M)

print(ans)

# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# arr_S = {input().strip() for _ in range(N)} # 집합 S에 문자열 저장
# count = sum(input().strip() in arr_S for _ in range(M)) # M개 문자열 검사 및 카운트
#
# print(count)