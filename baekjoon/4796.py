import sys

input = sys.stdin.readline

camping = []

while True:
	L, P, V = map(int, input().split())
	if L == 0:
		break
	camping.append((L, P, V))

# print(camping)


def camp(l, p, v):
	q = v // p
	r = v % p
	# 남은 일 수와 연속 가능한 일수를 비교해서 작은 수로 계산
	ans = l * q + min(r, l)
	return ans


for i in range(len(camping)):
	l, p, v = map(int, camping[i])
	print(f'Case {i+1}: {camp(l, p, v)}')

	# import sys
	#
	# input = sys.stdin.readline
	#
	#
	# def calculate_max_camping_days(L, P, V):
	# 	q = V // P
	# 	r = V % P
	# 	return L * q + min(r, L)
	#
	#
	# case_number = 1
	#
	# while True:
	# 	L, P, V = map(int, input().split())
	# 	if L == 0 and P == 0 and V == 0:
	# 		break
	#
	# 	max_days = calculate_max_camping_days(L, P, V)
	# 	print(f'Case {case_number}: {max_days}')
	# 	case_number += 1
