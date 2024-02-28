N = int(input())

count = 0

for _ in range(N):
	word = input()
	check_list = [word[0]]
	for i in range(len(word) - 1):
		if (word[i] != word[i + 1]) and (word[i + 1] not in check_list):
			check_list.append(word[i + 1])
		elif (word[i] != word[i + 1]) and (word[i + 1] in check_list):
			count += 1
			break


print(N - count)

# N = int(input())
#
# count = 0
#
# for _ in range(N):
#     word = input()
#     prev = ''  # 이전 문자를 저장할 변수
#     seen = set()  # 이미 나타난 문자를 저장할 세트
#     is_group_word = True  # 그룹 단어인지 판별할 변수
#     for char in word:
#         if char != prev:  # 현재 문자가 이전 문자와 다른 경우
#             if char in seen:  # 이미 나타난 문자인 경우
#                 is_group_word = False
#                 break
#             seen.add(char)  # 세트에 현재 문자 추가
#         prev = char  # 이전 문자를 현재 문자로 업데이트
#     if is_group_word:
#         count += 1  # 그룹 단어인 경우 카운트 증가
#
# print(count)
