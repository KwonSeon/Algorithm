import sys

input = sys.stdin.readline

N = int(input())
axis = []

for _ in range(N):
	x, y = map(int, input().split())
	axis.append([x, y])

axis.sort(key=lambda axis: (axis[1], axis[0]))

for i in range(N):
	print(*axis[i])

# import sys
#
# # 입력을 한 번에 받아옵니다.
# data = sys.stdin.read().splitlines()
#
# # 첫 번째 줄(점의 개수)을 제외한 나머지 줄에서 x, y 좌표를 분리하여 정수로 변환합니다.
# axis = [list(map(int, line.split())) for line in data[1:]]
#
# # y좌표, x좌표 순으로 정렬합니다.
# axis.sort(key=lambda x: (x[1], x[0]))
#
# # 결과를 문자열로 결합하여 출력합니다.
# sys.stdout.write('\n'.join(' '.join(map(str, x)) for x in axis))
