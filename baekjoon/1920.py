import sys

input = sys.stdin.readline

N = int(input())

arr = set(map(int, input().split()))

M = int(input())

check_list = list(map(int, input().split()))


def num_check(num, array):
	if num in array:
		print(1)
	else:
		print(0)


for num in check_list:
	num_check(num, arr)

# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# arr = set(map(int, input().split()))
# M = int(input())
# check_list = list(map(int, input().split()))
#
# result = []
#
# for num in check_list:
# 	result.append('1' if num in arr else '0')
#
# print('\n'.join(result))
