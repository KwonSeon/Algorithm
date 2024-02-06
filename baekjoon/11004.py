N, K = map(int, input().split())

lst = sorted(list(map(int, input().split())))
# lst.sort()

print(lst[K-1])