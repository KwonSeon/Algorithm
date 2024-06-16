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

# a, b = map(str, input().split())
#
# # A와 B의 길이 차이를 계산
# diff = len(b) - len(a)
#
# # 최소 차이를 저장할 변수
# min_difference = float('inf')
#
# # 가능한 모든 위치에서 A를 B에 맞춰본다.
# for i in range(diff + 1):
# 	count = 0
#
# 	# A와 B의 현재 위치에서의 차이를 계산
# 	for j in range(len(a)):
# 		if a[j] != b[j + i]:
# 			count += 1
#
# 	# 최소 차이를 갱신
# 	if count < min_difference:
# 		min_difference = count
#
# # 결과 출력
# print(min_difference)
