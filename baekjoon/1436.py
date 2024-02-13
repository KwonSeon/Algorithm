N = int(input())

x = 666
count = 1

while count <= N:
	if count == N:
		print(x)
		break
	x += 1
	if '666' in str(x):
		count += 1

