import sys

input = sys.stdin.readline

N = int(input())

card_list = list(map(int, input().split()))

M = int(input())

print_arr = list(map(int, input().split()))

# print(card_list)
# print(print_arr)

ans = {}

for i in range(N):
	card = card_list[i]
	if card not in ans:
		ans[card] = 1
	else:
		ans[card] += 1

# print(ans)

ans_list = []

for num in print_arr:
	if num in ans:
		ans_list.append(ans[num])
	else:
		ans_list.append(0)

print(*ans_list)