a, b = map(str, input().split())

diff = len(b) - len(a)

ans = []

for i in range(diff + 1):
	count = 0

	for j in range(len(a)):
		if a[j] != b[j + i]:
			count += 1

	ans.append(count)

print(min(ans))