n = int(input())
case_arr = list(map(int, input().split()))
case_arr.sort()
target_n = n // 2
print(case_arr[target_n])