S = input()

# print(int(len(S)/2))

max_length = 0

for i in range(len(S)):
	for j in range(i+2, len(S)+1, 2):
		sub_S = S[i:j]
		# print(sub_S)
		mid = len(sub_S) // 2
		left_sum = sum(int(digit) for digit in sub_S[:mid])
		right_sum = sum(int(digit) for digit in sub_S[mid:])

		if left_sum == right_sum:
			max_length = max(max_length, len(sub_S))

print(max_length)