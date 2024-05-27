def check_bracket(sentence):
    stack = []

    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return 'no'
            stack.pop()
        elif char == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return 'no'
            stack.pop()
        elif char == '.':
            break

    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'

import sys
input = sys.stdin.read

def main():
    lines = input().split('\n')
    for line in lines:
        if line == '.':
            break
        print(check_bracket(line))

if __name__ == "__main__":
    main()
