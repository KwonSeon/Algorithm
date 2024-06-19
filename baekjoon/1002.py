import sys
import math

input = sys.stdin.readline

t = int(input().strip())


def turret():
	x1, y1, r1, x2, y2, r2 = map(int, input().split())

	if x1 == x2 and y1 == y2 and r1 == r2:
		return -1
	elif x1 == x2 and y1 == y2 and r1 != r2:
		return 0

	d1 = math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))
	d2 = r1 + r2

	if d1 > d2:
		return 0
	elif d1 == d2:
		return 1
	else:
		if d1 + min(r1, r2) == max(r1, r2):
			return 1
		elif d1 + min(r1, r2) < max(r1, r2):
			return 0
		else:
			return 2


for _ in range(t):
	print(turret())


# def find_intersection_count(x1, y1, r1, x2, y2, r2):
# 	dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
# 	sum_r = r1 + r2
# 	diff_r = abs(r1 - r2)
#
# 	if dist_sq == 0 and r1 == r2:
# 		return -1  # 무한대의 교점
# 	elif dist_sq > sum_r ** 2 or dist_sq < diff_r ** 2:
# 		return 0  # 교점 없음
# 	elif dist_sq == sum_r ** 2 or dist_sq == diff_r ** 2:
# 		return 1  # 한 개의 교점
# 	else:
# 		return 2  # 두 개의 교점
#
#
# T = int(input())
# for _ in range(T):
# 	x1, y1, r1, x2, y2, r2 = map(int, input().split())
# 	print(find_intersection_count(x1, y1, r1, x2, y2, r2))