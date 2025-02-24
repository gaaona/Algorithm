T = int(input())

for tc in range(T):
    txt = input()
    stack = []
    printing_line = ''
    N = len(txt)

    for i in range(N):
        if txt[i] == ' ':
            while stack:
                printing_line += stack.pop()
            printing_line += ' '
        else:
            stack.append(txt[i])

    while stack:
        printing_line += stack.pop()

    print(printing_line)