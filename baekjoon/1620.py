import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_dict = {}

# print(pokemon)

num = 1
while num <= N:
	pokemon = input().strip()
	pokemon_dict[pokemon] = num
	num += 1

pokemon_list = list(pokemon_dict.keys())
# print(pokemon_arr)

for _ in range(M):
	question = input().strip()
	if question.isdigit():
		print(pokemon_list[int(question) - 1])
	else:
		print(pokemon_dict[question])


# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# pokemon_name_to_num = {}  # 이름으로 번호를 찾는 딕셔너리
# pokemon_num_to_name = {}  # 번호로 이름을 찾는 딕셔너리
#
# for num in range(1, N + 1):
#     pokemon = input().strip()
#     pokemon_name_to_num[pokemon] = num
#     pokemon_num_to_name[num] = pokemon
#
#
# for _ in range(M):
#     question = input().strip()
#     if question.isdigit():
#         print(pokemon_num_to_name[int(question)])
#     else:
#         print(pokemon_name_to_num[question])
