import sys

input = sys.stdin.readline

N, M = map(int, input().split())

non_lis = set(input().strip() for _ in range(N))
ans = []
# print(non_lis)

for _ in range(M):
	name = input().strip()
	if name in non_lis:
		ans.append(name)

ans.sort()
print(len(ans))
print(*ans, sep='\n')

# import sys
#
#
# def read_input():
# 	return sys.stdin.readline().strip()
#
#
# def main():
# 	N, M = map(int, read_input().split())
# 	unheard = {read_input() for _ in range(N)}
# 	unseen = {read_input() for _ in range(M)}
#
# 	unheard_and_unseen = sorted(unheard & unseen)
# 	print(len(unheard_and_unseen))
# 	print('\n'.join(unheard_and_unseen))
#
#
# if __name__ == "__main__":
# 	main()