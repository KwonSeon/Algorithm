transcript = [list(map(str, input().split())) for _ in range(20)]

# print(transcript)


def caculator(C, G):
	if G == 'A+':
		return C, 4.5
	elif G == 'A0':
		return C, 4.0
	elif G == 'B+':
		return C, 3.5
	elif G == 'B0':
		return C, 3.0
	elif G == 'C+':
		return C, 2.5
	elif G == 'C0':
		return C, 2.0
	elif G == 'D+':
		return C, 1.5
	elif G == 'D0':
		return C, 1.0
	elif G == 'F':
		return C, 0
	elif G == 'P':
		return 0, 0


credit = 0
grad = []
for i in range(20):
	c, g = caculator(int(float(transcript[i][1])), transcript[i][2])
	credit += c
	grad.append(c * g)

gpa = sum(grad) / credit

print(gpa)

# def calculator(C, G):
#     grade_points = {
#         'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
#         'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,
#         'F': 0, 'P': None
#     }
#     return C, grade_points.get(G, 0)  # 'G'에 해당하는 점수 반환, 없으면 0 반환
#
# transcript = [list(map(str, input().split())) for _ in range(20)]
#
# credit = 0
# grad = []
# for course, c, g in transcript:
#     c = float(c)  # 학점을 float으로 변환
#     c, g = calculator(c, g)
#     if g is not None:  # 'P' 등급 과목은 제외
#         credit += c
#         grad.append(c * g)
#
# if credit > 0:
#     gpa = sum(grad) / credit
#     print(gpa)
# else:
#     print("학점을 얻은 과목이 없습니다.")