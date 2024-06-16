# import sys
#
# input = sys.stdin.readline
#
# n = int(input().strip())
#
# card_dic = {}
#
# for _ in range(n):
# 	num = int(input().strip())
# 	if num in card_dic:
# 		card_dic[num] += 1
# 	else:
# 		card_dic[num] = 1
#
# sorted_card = sorted(card_dic.items(), key=lambda x:(-x[1], x[0]))
#
# print(sorted_card[0][0])

import sys
from collections import Counter

input = sys.stdin.readline

# 숫자 카드의 개수 입력
n = int(input().strip())

# 숫자 카드의 빈도를 저장할 Counter
card_counter = Counter([int(input().strip()) for _ in range(n)])

# most_common 메서드로 빈도 계산 후 정렬
common_card = card_counter.most_common()
common_card.sort(key=lambda x: (-x[1], x[0]))

# 가장 빈번한 숫자 출력
print(common_card[0][0])
