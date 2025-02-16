T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    
    max_count = 1
    cnt = 1
    
    for i in range(N-1):
        if C[i + 1] > C[i]:
            cnt += 1
            if max_count < cnt:
                max_count = cnt
        else:
            cnt = 1

    print(f'#{tc} {max_count}')
