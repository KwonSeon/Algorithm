N = input()

arr = []

for i in range(len(N)):
	arr.append(N[i])

arr = sorted(arr, reverse=True)

ans = ''.join(arr)

print(ans)

# N = input()
# sorted_N = ''.join(sorted(N, reverse=True))
# print(sorted_N)
