N = int(input())


def is_good_word(word):
    stack = []
    for char in word:
        if stack and stack[-1] == char:  # 스택이 비어있지 않고, 마지막 문자와 현재 문자가 같으면 짝을 이룸
            stack.pop()  # 짝을 이룬 문자 제거
        else:
            stack.append(char)  # 스택에 현재 문자 추가
    return 1 if not stack else 0  # 스택이 비어있으면 좋은 단어


good_word_count = sum(is_good_word(input()) for _ in range(N))

print(good_word_count)