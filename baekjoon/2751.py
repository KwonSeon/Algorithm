import sys
input = sys.stdin.readline

N = int(input())

ans = [int(input()) for _ in range(N)]
ans = sorted(ans)

for i in range(N):
	print(ans[i])

# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# ans = [int(input()) for _ in range(N)]
# ans.sort()  # In-place 정렬로 메모리 사용량을 약간 줄일 수 있음
#
# print('\n'.join(map(str, ans)))
