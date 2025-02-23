pair_dict = {'(':')', '[':']'}

def print_is_balanced(line):
    stack = []

    for char in line: # str에서 처리
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack or pair_dict[stack.pop()] != char: # 스택이 비었거나(여는 괄호 없음) 짝이 안맞으면
                return 'no'
        else: continue

    return 'yes' if not stack else 'no' # 스택이 비었으면 yes 아니면  no

while True:
    input_txt = input() # 종료 조건 식별을 위해 input 그대로

    if input_txt == '.':
        break
    else:
        print(print_is_balanced(input_txt))