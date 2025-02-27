import sys
from collections import deque

def process_command():
    commands = list(sys.stdin.readline().split())
    com = commands[0] # 매번 쳐야해서 변수로 할당
    if com == 'push_front':
        return q.appendleft(int(commands[1]))
    elif com == 'push_back':
        return q.append(int(commands[1]))
    elif com == 'pop_front':
        if q:
            return q.popleft()
        else:
            return -1
    elif com == 'pop_back':
        if q:
            return q.pop()
        else:
            return -1
    elif com == 'size':
        return len(q)
    elif com == 'empty':
        if q:
            return 0
        else:
            return 1
    elif com == 'front':
        if q:
            return q[0]
        else:
            return -1
    elif com == 'back':
        if q:
            return q[-1]
        else:
            return -1
    return -2 # return 없이 끝나니까 허전해서.... 디버깅용

N = int(sys.stdin.readline())
q = deque()

for _ in range(N):
    result = process_command() # 그냥 print했더니 None이 나옴

    if result is not None: # 그냥 if result: 했더니 0인 경우 출력 안됨
        print(result)