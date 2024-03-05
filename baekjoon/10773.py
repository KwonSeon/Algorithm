import sys

input = sys.stdin.readline

K = int(input())

arr = []

for _ in range(K):
	num = int(input())
	if num == 0:
		arr.pop()
	else:
		arr.append(num)

print(sum(arr))

# import sys
# from collections import deque
#
# input = sys.stdin.readline
# K = int(input())
#
# # deque를 사용하여 arr 초기화
# arr = deque()
#
# for _ in range(K):
#     num = int(input())
#     if num == 0:
#         arr.pop()  # 가장 최근에 추가된 요소 제거
#     else:
#         arr.append(num)  # 새 요소 추가
#
# print(sum(arr))