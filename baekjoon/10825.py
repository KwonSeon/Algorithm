import sys

input = sys.stdin.readline

n = int(input().strip())
lst = [tuple(map(str, input().split())) for _ in range(n)]


lst.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

ans = [lst[i][0] for i in range(n)]

print(*ans, sep='\n')

# import sys
#
# input = sys.stdin.readline
#
# # 학생 수 입력
# n = int(input().strip())
#
# # 학생 정보 입력
# students = []
# for _ in range(n):
#     name, korean, english, math = input().strip().split()
#     students.append((name, int(korean), int(english), int(math)))
#
# # 정렬 기준에 따라 정렬
# students.sort(key=lambda student: (-student[1], student[2], -student[3], student[0]))
#
# # 정렬된 학생들의 이름 출력
# for student in students:
#     print(student[0])
