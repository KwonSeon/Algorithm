import sys

input = sys.stdin.readline

N, Kim, Yim = map(int, input().split())

round_num = 1


def game(num1, num2, count):
	if (num1 % 2 == 1) and (num2 == num1 + 1):
		print(count)
	elif num1 < 1:
		print(-1)
	else:
		if num1 % 2 == 0:
			num1= num1 / 2
		elif num1 % 2 == 1:
			num1 = (num1 + 1) / 2
		if num2 % 2 == 0:
			num2= num2 / 2
		elif num2 % 2 == 1:
			num2 = (num2 + 1) / 2
		count += 1
		game(num1, num2, count)


game(min(Kim, Yim), max(Kim, Yim), round_num)

# N, Kim, Yim = map(int, input().split())
#
# round_num = 0
#
# # 라운드를 반복하면서 김지민과 임한수의 번호를 업데이트합니다.
# # 두 번호가 같아질 때까지 라운드를 계속 진행합니다.
# while Kim != Yim:
#     # 각 라운드마다 번호를 업데이트합니다.
#     # 홀수 번호는 +1을 하여 짝수로 만든 후 2로 나눕니다.
#     Kim = (Kim + 1) // 2
#     Yim = (Yim + 1) // 2
#     round_num += 1
#
# print(round_num)