T = int(input())
 
for test_case in range(1, T+1):
 
    di = [0, 1, 1, 0]
    dj = [0, 0, 1, 1]
 
    N, M = map(int, input().split())
 
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    # 한 행에서 가장 큰 이웃
    max_fly = 0
    for i in range(N-M+1): # 기준 칸이 이동할 수 있는 최대 범위 인덱스
 
        for j in range(N-M+1): # 기준 칸이 이동할 수 있는 최대 범위 인덱스
            section_sum = 0              # 영역의 합
            for p in range(M):
                for q in range(M):
                    section_sum += arr[i+p][j+q]
            if max_fly < section_sum:
                max_fly = section_sum
 
    print(f'#{test_case} {max_fly}')