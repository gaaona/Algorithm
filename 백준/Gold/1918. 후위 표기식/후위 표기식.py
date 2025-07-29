import sys
line = sys.stdin.readline().strip()

stack = [0]*100 # 최대 길이가 100
top = -1

incoming_priority = {'(': 3, '*': 2, '/':2, '+':1, '-':1} # 현재 문자(char)
stack_priority = {'(': 0, '*': 2, '/':2, '+':1, '-':1} # 이미 스택에 들어간 문자

ans = ""

for char in line:
    if char not in '(*/+-)': # 피연산자에 없는 경우(문자인 경우)
        ans += char
    elif char == ')': # 닫는 괄호인 경우(연산해야 됨)
        while stack[top] != '(': # 여는 괄호 전까지
            ans += stack[top] # 이어붙이기
            top -= 1
        top -= 1 # 여는 괄호까지 빼주기
    else:
        if top == -1 or stack_priority[stack[top]] < incoming_priority[char]: # stack이 빔 or char가 스택에 있는 거보다 우선
            top += 1
            stack[top] = char
        elif stack_priority[stack[top]] >= incoming_priority[char]: # 스택 우선순위가 더 높음
            while top > -1 and stack_priority[stack[top]] >= incoming_priority[char]:
                ans += stack[top]
                top -= 1
            top += 1
            stack[top] = char
            
if top > -1: # stack에 아직 남아 있는 경우
    while top > -1 and stack[top] != '(': # 스택이 아직 안 비었고 닫는 괄호가 아닌 경우
        ans += stack[top]
        top -= 1
print(ans)