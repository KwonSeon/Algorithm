N = int(input())

ans = []
counter = 0

for _ in range(N):
	age, name = map(str, input().split())
	ans.append((int(age), counter, name)) # int를 사용하지 않으면 2, 10에서 10, 2 순서대로 정렬된다
	counter += 1

ans.sort()

# print(ans)
for i in range(N):
	print(ans[i][0], ans[i][2])



# N = int(input())
# members = []
#
# for _ in range(N):
#     age, name = input().split()
#     age = int(age)
#     members.append((age, name))
#
# # 나이를 기준으로 회원 정보를 정렬합니다. Python의 sort() 메소드는 기본적으로 안정 정렬을 사용합니다.
# members.sort(key=lambda member: member[0])
#
# for age, name in members:
#     print(age, name)
