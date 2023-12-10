import sys

input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

# 예산 요청이 총액을 넘지 않는 경우
if sum(budgets) <= M:
  print(max(budgets))
else:
  low, high = 0, max(budgets)
  while low <= high:
    mid = (low + high) // 2
    total = sum(min(budget, mid) for budget in budgets)

    if total <= M:
      low = mid + 1
    else:
      high = mid - 1

  print(high)
