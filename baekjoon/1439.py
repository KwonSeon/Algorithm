# S = input()
# S0 = S.split('1')
# S1 = S.split('0')
# while '' in S0:
# 	S0.remove('')
# while '' in S1:
# 	S1.remove('')
#
# # print(S0)
# # print(S1)
#
# ans = min(len(S0), len(S1))
#
# print(ans)

S = input()

# '0'에서 '1' 또는 '1'에서 '0'으로 바뀌는 지점의 수를 세기
count = 0
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        count += 1

# 첫 번째 문자도 덩어리의 시작으로 간주하기 위해 count를 1 증가
count += 1

# 덩어리의 수를 2로 나누어 최소 뒤집기 횟수 계산
ans = count // 2

print(ans)
