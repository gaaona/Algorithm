def reverse_print():
    global top, complete_txt, stack # 수정하려는 global 변수들
    while top > -1: # stack이 빌 때까지
        complete_txt += stack[top]
        top -= 1

S = input()
N = len(S)

complete_txt = ''
i = 0
stack = [''] * (N + 1)
# print(stack)
top = -1

while i < N:
    if S[i] == '<': # 똑바로 출력되는 부분
        reverse_print() # 제대로 출력하기 위해 stack 출력해서 비우기

        while i < N and S[i] != '>':
            complete_txt += S[i]
            i += 1
        if S[i] == '>': # 닫는 기호까지 더하기
            complete_txt += S[i]
            i += 1
    elif S[i] == ' ': # 단어 단위로 뒤집을 거라 공백을 만나면
        reverse_print()
        complete_txt += ' ' # 단어 끝나면 공백 추가
        i += 1
    else: # 일반 단어
        top += 1
        stack[top] = S[i]
        i += 1

# S는 다 읽어도 stack이 쌓여있는 경우가 있음
reverse_print() # 남은 스택 비우기

print(complete_txt)