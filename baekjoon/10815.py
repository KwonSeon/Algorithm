import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
card_lists = list(map(int, input().split()))
card_lists.sort()
M = int(input())
find_card_lists = list(map(int, input().split()))


# print(f'N:{N} \n card_lists:{card_lists} \n M:{M} \n find_card_lists:{find_card_lists}')

ans = []
for find_card_list in find_card_lists:
	l = bisect_left(card_lists, find_card_list)
	r = bisect_right(card_lists, find_card_list)
	ans.append(1 if r>l else 0)

print(*ans)
print(' '.join(map(str, ans)))