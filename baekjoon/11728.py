N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(A + B)

# ans = set(A + B) 중복 제거하면 틀림
ans = A + B
ans = sorted(ans)

print(*ans)