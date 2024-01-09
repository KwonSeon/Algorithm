def find_max_people(coconuts):
    k = 2
    answer = []

    while k < coconuts:
        coconut = coconuts
        for i in range(k):
            coconut -= 1  # 원숭이에게 한 개 줌
            coconut -= coconut // k  # 내 몫을 제외하고 나머지

            if (coconut - 1) % k != 0:
                if i == k - 1:
                    answer.append(k)
                break
        k += 1

    if answer:
        return f"{coconuts} coconuts, {answer[-1]} people and 1 monkey"
    else:
        return f"{coconuts} coconuts, no solution"

# 사용자 입력 받기
while True:
    n = input()
    if n == '-1':
        break
    else:
        coconut_count = int(n)
        print(find_max_people(coconut_count))
