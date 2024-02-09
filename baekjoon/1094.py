X = int(input())


def f(total_stick, target):
	if sum(total_stick) == target:
		print(len(total_stick))
	elif sum(total_stick) > target:
		total_stick[-1] = total_stick[-1] / 2
		total_stick.append(total_stick[-1])
		if sum(total_stick[:-1]) >= target:
			total_stick.remove(total_stick[-1])
			f(total_stick, target)
		else:
			f(total_stick, target)


f([64], X)
