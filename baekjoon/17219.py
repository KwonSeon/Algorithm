import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ans = {}

for _ in range(N):
	url, password = map(str, input().split())
	ans[url] = password

# print(ans)

for _ in range(M):
	url = input().strip()
	print(ans[url])

# import sys
#
# # 입력 받기
# N, M = map(int, sys.stdin.readline().split())
#
# # 사이트 주소와 비밀번호 저장
# passwords = {}
# for _ in range(N):
#     site, pwd = sys.stdin.readline().split()
#     passwords[site] = pwd
#
# # 비밀번호 출력
# for _ in range(M):
#     site = sys.stdin.readline().strip()
#     sys.stdout.write(passwords[site] + '\n')
