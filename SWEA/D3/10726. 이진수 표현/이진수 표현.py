T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    if bin(M)[-N:] == ('1' * N):
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')