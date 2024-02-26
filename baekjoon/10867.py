import sys
input = sys.stdin.readline

N = int(input())

ans = set(map(int, input().split()))

ans = sorted(ans)

print(*ans)