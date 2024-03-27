N = int(input())

length = len(str(N))

count_num = N - (10 ** (length - 1)) + 1

# print(count_num)

counted_last_num = 0
i = 1

while i < length:
	calculed_num = 9 * i * (10 ** (i-1))
	counted_last_num += calculed_num
	i+=1
	# print(counted_last_num)

ans = count_num * length + counted_last_num

print(int(ans))

