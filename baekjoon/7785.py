import sys

input = sys.stdin.readline

n = int(input())
total_list = []


def log_check(x, lst):
	name, log = x.split()
	if log == 'enter':
		lst.append(name)
	elif log == 'leave':
		lst.remove(name)


for _ in range(n):
	log_check(input(), total_list)

total_list.sort()

for _ in range(len(total_list)):
	print(total_list.pop())