import sys
input = sys.stdin.readline

M = int(input())

S = []


def f(op, X, S):
	if op == 'add':
		if X not in S:
			S.append(X)
	elif op == 'remove':
		if X in S:
			S.remove(X)
	elif op == 'check':
		if X in S:
			print(1)
		else:
			print(0)
	elif op == 'toggle':
		if X in S:
			S.remove(X)
		else:
			S.append(X)


for _ in range(M):
	operator = list(map(str, input().split()))
	if operator[0] == 'all':
		S = [i for i in range(1, 21)]
	elif operator[0] == 'empty':
		S = []
	else:
		x = int(operator[1])
		f(operator[0], x, S)

# import sys
# input = sys.stdin.readline
#
# M = int(input())
#
# S = set()
#
#
# def f(op, X, S):
#     if op == 'add':
#         S.add(X)
#     elif op == 'remove':
#         S.discard(X)  # remove와 유사하지만, X가 S에 없어도 에러가 발생하지 않음
#     elif op == 'check':
#         if X in S:
#             print(1)
#         else:
#             print(0)
#     elif op == 'toggle':
#         if X in S:
#             S.remove(X)
#         else:
#             S.add(X)
#
#
# for _ in range(M):
#     operator = input().split()
#     if operator[0] == 'all':
#         S = set(range(1, 21))
#     elif operator[0] == 'empty':
#         S = set()
#     else:
#         x = int(operator[1])
#         f(operator[0], x, S)
