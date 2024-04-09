N = int(input().strip())

ans = 0
if N < 100:
	ans = N
else:
	ans = 99
	for i in range(100, N + 1):
		str_i = str(i)
		len_str = len(str_i)
		first_num = str_i[0]
		second_num = str_i[1]
		cd = int(second_num) - int(first_num)
		for i in range(2, len_str):
			if int(str_i[i]) - int(str_i[i - 1]) != cd:
				break
			ans += 1

print(ans)

# def is_hansu(number):
#     if number < 100:
#         return True  # 100 미만의 모든 수는 한수입니다.
#     digits = list(map(int, str(number)))
#     common_difference = digits[1] - digits[0]
#     for i in range(2, len(digits)):
#         if digits[i] - digits[i-1] != common_difference:
#             return False
#     return True
#
# N = int(input().strip())
# hansu_count = sum(is_hansu(i) for i in range(1, N+1))
# print(hansu_count)