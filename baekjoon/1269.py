import sys

input = sys.stdin.readline

A, B = map(int, input().split())

A_arr = set(map(int, input().split()))
B_arr = set(map(int, input().split()))

# print(A_arr - B_arr)
# print(B_arr - A_arr)

len_A = len(A_arr - B_arr)
len_B = len(B_arr - A_arr)

len = len_A + len_B

print(len)

# import sys
#
# input = sys.stdin.readline
#
# A, B = map(int, input().split())
# A_arr = set(map(int, input().split()))
# B_arr = set(map(int, input().split()))
#
# # 대칭 차집합의 길이를 계산하여 출력
# print(len(A_arr ^ B_arr))
