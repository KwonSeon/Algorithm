N = input()

ans = [0] * 9

for i in range(len(N)):
	num = int(N[i])
	if num == 9:
		num = 6
	ans[num] += 1

cal = ans[6]

if (ans[6] % 2) == 0:
	ans[6] = cal // 2
else:
	ans[6] = (cal + 1) // 2

print(int(max(ans)))