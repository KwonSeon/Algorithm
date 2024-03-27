import sys

input = sys.stdin.readline

N, M = map(int, input().split())


# 최저가를 계산
min_six_strings = 1001
min_one_strings = 1001

for _ in range(M):
	six_strings, one_string = map(int, input().split())
	if six_strings < min_six_strings:
		min_six_strings = six_strings
	if one_string < min_one_strings:
		min_one_strings = one_string

# 6개 패키지 가격보다 낱개로 구매했을 때가 싼 경우
total_cost_single = N * min_one_strings

# 전체 패키지로만 구매할 때
total_cost_package = ((N + 5) // 6) * min_six_strings

# 패키지와 낱개의 조합으로 구매할 때
total_cost_mix = (N // 6) * min_six_strings + (N % 6) * min_one_strings

# 최소 비용
min_total_cost = min(total_cost_package, total_cost_mix, total_cost_single)

print(min_total_cost)