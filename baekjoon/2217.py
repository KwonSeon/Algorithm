import sys

input = sys.stdin.readline

N = int(input())

rope = [int(input()) for _ in range(N)]
rope.sort(reverse=True)

ans = []

# 가작 작은 수 * 개수를 곱하여 버틸 수 있는
# 중량을 구한 후 그 중 최대값을 출력
# print(rope)

while rope:
	cnt = len(rope)
	min_rope = rope.pop()
	ans.append(cnt * min_rope)

max_weight = max(ans)

print(max_weight)