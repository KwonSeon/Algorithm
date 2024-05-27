import sys
input = sys.stdin.readline

N = int(input().strip())

card_list = {}

for _ in range(N):
	num = int(input().strip())
	if num in card_list:
		card_list[num] += 1
	else:
		card_list[num] = 1


sorted_card = sorted(card_list.items())

print(sorted_card)

for i in range(1, len(sorted_card)):
	pre_num = sorted_card[i - 1][0]
	pre_count = sorted_card[i - 1][1]

	cur_num = sorted_card[i][0]
	cur_count = sorted_card[i][1]

	if pre_count != cur_count:
		print(pre_num)
		break
