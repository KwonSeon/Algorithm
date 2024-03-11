# import sys
# import math
#
# input = sys.stdin.readline
#
# t = int(input())
#
# for i in range(t):
# 	arr = list(map(int, input().split()))
# 	gcd = []
# 	# print(arr)
# 	for j in range(1, len(arr)):
# 		for k in range(j + 1, len(arr)):
# 			num = math.gcd(arr[j], arr[k])
# 			gcd.append(num)
# 	print(sum(gcd))

import sys
import math

# 입력 빠르게 받기
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # 입력 받은 후 첫 번째 요소(수의 개수)는 무시하고 나머지 수를 사용
    arr = list(map(int, input().split()))[1:]
    gcd_sum = 0  # GCD의 합을 저장할 변수

    # 가능한 모든 쌍의 GCD를 계산하여 합산
    for j in range(len(arr)):
        for k in range(j + 1, len(arr)):
            gcd_sum += math.gcd(arr[j], arr[k])

    print(gcd_sum)
