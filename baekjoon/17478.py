N = int(input())

arr = [
	'"재귀함수가 뭔가요?"',
	'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
	'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
	'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
]


def replay(n, count, sentences):
	if count == 0:
		print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
	if n == count:
		print(('____' * count) + sentences[0])
		print(('____' * count) + '"재귀함수는 자기 자신을 호출하는 함수라네"')
		print(('____' * count) + '라고 답변하였지.')
	else:
		for sentence in sentences:
			print(('____' * count) + sentence)
		replay(n, count+1, sentences)
		print(('____' * count) + '라고 답변하였지.')

replay(N, 0, arr)

# def print_message(depth, current=0):
#     indent = "____" * current
#     if current == depth:  # 종료 조건에 도달했을 때
#         print(f"{indent}\"재귀함수가 뭔가요?\"")
#         print(f"{indent}\"재귀함수는 자기 자신을 호출하는 함수라네\"")
#         print(f"{indent}라고 답변하였지.")
#         return
#
#     # 재귀 호출 전 공통 메시지 출력
#     print(f"{indent}\"재귀함수가 뭔가요?\"")
#     print(f"{indent}\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
#     print(f"{indent}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
#     print(f"{indent}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
#
#     # 재귀 호출
#     print_message(depth, current + 1)
#
#     # 재귀 호출 후 종료 시 메시지 출력
#     print(f"{indent}라고 답변하였지.")
#
# # 입력 받기
# N = int(input())
# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# print_message(N)
