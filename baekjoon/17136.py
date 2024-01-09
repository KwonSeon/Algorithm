# 보드의 크기는 항상 10x10입니다.
N = 10
# 사용자로부터 10x10 보드 상태를 입력받습니다. 1은 색종이를 붙여야 할 부분, 0은 빈 부분입니다.
board = [list(map(int, input().split())) for _ in range(N)]

# 각 크기의 색종이가 몇 장 남았는지 저장하는 배열입니다. 처음에는 각각 5장씩 있습니다.
papers = [0, 5, 5, 5, 5, 5]

# 정답을 저장할 변수입니다. 가능한 최대 값으로 초기화합니다.
answer = float('inf')

def is_valid(x, y, size):
    # (x, y) 위치에서 size 크기의 색종이를 붙일 수 있는지 확인합니다.
    # 색종이가 보드를 벗어나거나, 빈 칸을 덮으면 안됩니다.
    for i in range(x, x + size):
        for j in range(y, y + size):
            if i >= N or j >= N or board[i][j] != 1:
                return False
    return True

def set_paper(x, y, size, state):
    # (x, y) 위치에 size 크기의 색종이를 붙이거나 떼는 함수입니다.
    # state가 0이면 색종이를 붙이고, 1이면 색종이를 뗍니다.
    for i in range(x, x + size):
        for j in range(y, y + size):
            board[i][j] = state

def backtrack(x, y, count):
    global answer
    # (x, y)는 현재 탐색 중인 보드의 위치입니다.
    # count는 현재까지 사용한 색종이의 수입니다.
    if y == N:
        # 한 행을 모두 탐색했다면, 다음 행으로 넘어갑니다.
        x += 1
        y = 0
    if x == N:
        # 모든 칸을 탐색했다면, 현재까지의 색종이 수를 최소값과 비교하여 갱신합니다.
        answer = min(answer, count)
        return
    if board[x][y] == 1:
        # 현재 위치에 색종이를 붙여야 하는 경우
        for size in range(1, 6):
            # 사용 가능한 모든 크기의 색종이에 대해 시도합니다.
            if papers[size] > 0 and is_valid(x, y, size):
                # 색종이를 붙이고, 다음 칸으로 넘어갑니다.
                set_paper(x, y, size, 0)
                papers[size] -= 1
                backtrack(x, y + size, count + 1)
                # 백트래킹: 색종이를 떼고, 이전 상태로 되돌립니다.
                set_paper(x, y, size, 1)
                papers[size] += 1
    else:
        # 현재 위치에 색종이를 붙일 필요가 없는 경우
        backtrack(x, y + 1, count)

# 백트래킹 시작
backtrack(0, 0, 0)
# 가능한 최소 색종이 수 출력, 불가능한 경우 -1 출력
print(answer if answer != float('inf') else -1)
