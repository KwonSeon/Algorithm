import sys

input = sys.stdin.readline

n, m = map(int,input().split())

arr = list(map(int, input().split()))

start, end = 0, 0
current_sum = 0
count = 0

while end < n:
	if current_sum < m:
		current_sum += arr[end]
		end += 1

	elif current_sum == m:
		count += 1
		current_sum -= arr[start]
		start += 1

	else:
		current_sum -= arr[start]
		start += 1
	# print(f'start: {start}, end: {end}, current_sum: {current_sum}, count: {count}')

# while start < n:
# 	if current_sum > m:
# 		current_sum -= arr[start]
# 		start+= 1
#
# 	elif current_sum == m:
# 		count += 1
# 		break
#
# 	else:
# 		break

# 마지막 부분 배열 확인
while current_sum >= m and start < n:
	if current_sum == m:
		count += 1
	current_sum -= arr[start]
	start += 1

print(count)