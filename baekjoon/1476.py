E, S, M = map(int, input().split())
#
# print(3*5*2*2*7*19)
#
# 15 15 15 15
# 1 16 16 16
# 4 19 19 19
# 5 20 1 20
# 13 28 9 28
# 14 1 10 29
# 15 2 11 30
# 1 3 12 31
# 8 10 19 38
# 9 11 1 39
# 15 17 7 45
# 1 18 8 46
# 11 28 18 56
# 12 1 19 57
# 13 2 1 58
# 15 4 3 60
# 1 5 4 61


# e, s, m = 1, 1, 1
# ans = 1
#
# while True:
# 	if e == 16:
# 		e = 1
# 	elif s == 29:
# 		s = 1
# 	elif m == 20:
# 		m = 1
#
# 	if E == e and S == s and M == m:
# 		break
#
# 	e += 1
# 	s += 1
# 	m += 1
# 	ans += 1
#
# print(ans)

# 나머지가 E, S, M 일 때, 계산을 하고 안 맞으면 추가로 값을 더해서 계산

# ans = E
# e, s, m = E, E, E
# while True:
# 	if (s % 28) == S and (m % 19) == M:
# 		print(ans)
# 		break
# 	ans += 15
# 	s += 15
# 	m += 15

def calculate_year(E, S, M):
    e, s, m = 1, 1, 1
    year = 1
    while True:
        if e == E and s == S and m == M:
            return year
        e, s, m = e % 15 + 1, s % 28 + 1, m % 19 + 1
        year += 1


print(calculate_year(E, S, M))