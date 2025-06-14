for tc in range(1, 11):
    N = int(input())
    cryptos = list(map(int, input().split()))

    M = int(input())
    commands = input().split()
    idx = 0
    
    while idx < len(commands):
        if commands[idx] == 'I':
            x = int(commands[idx+1])
            y = int(commands[idx+2])
            s = list(map(int, commands[idx+3:idx+3+y]))
            cryptos[x:x] = s  # in-place 삽입
            idx += 3 + y
        elif commands[idx] == 'D':
            x = int(commands[idx+1])
            y = int(commands[idx+2])
            del cryptos[x:x+y]  # in-place 삭제
            idx += 3
        elif commands[idx] == 'A':
            y = int(commands[idx+1])
            s = list(map(int, commands[idx+2:idx+2+y]))
            cryptos.extend(s)  # in-place 추가
            idx += 2 + y

    print(f'#{tc}', *cryptos[:10])
