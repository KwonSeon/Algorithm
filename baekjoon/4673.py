# d(n)이 이미 계산된 생성자를 만든다면 그 이후의 계산도 같으므로 다시 계산하지 않아도 된다.
self = [0] * 10001


# 자릿수 더하는 함수
def sum_of_digits(n):
	ans = 0
	while n > 0:
		ans += n % 10
		n //= 10
	return ans

for i in range(1, 10001):
	k = i
	while True:
		j = k + sum_of_digits(k)
		if j > 10000 or self[j] ==1:
			break
		elif self[j] == 0:
			self[j] += 1
		k = j


for i in range(1, 10001):
	if self[i] == 0:
		print(i)