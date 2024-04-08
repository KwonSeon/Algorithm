import sys

input = sys.stdin.readline

N = input().strip()

# N = list(map(int,  input().split()))
digits = list(N)
digits.sort(reverse=True)
# print(digits)

# 0이 포함되어 있는지와 숫자들의 합이 3으로 나누어 떨어지는지 확인
if "0" not in digits or sum(map(int, digits)) % 3 != 0:
    print(-1)
else:
    print("".join(digits))