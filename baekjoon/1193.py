X = int(input())

# 대각선의 끝 번호와 대각선에 있는 분수의 개수를 찾음
line = 0  # 대각선 번호
max_num = 0  # 그 대각선에서의 최대 번호
while X > max_num:
    line += 1
    max_num += line

# 대각선 내에서 X의 위치를 찾음
gap = max_num - X

# 짝수번째 대각선과 홀수번째 대각선일 때의 분자와 분모를 결정
if line % 2 == 0:
    top = line - gap  # 분자
    bottom = gap + 1  # 분모
else:
    top = gap + 1  # 분자
    bottom = line - gap  # 분모

print(f'{top}/{bottom}')
