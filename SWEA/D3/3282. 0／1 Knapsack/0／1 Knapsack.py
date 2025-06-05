T = int(input())
 
for tc in range(1,T+1):
    N,K = map(int, input().split())
 
    V = [0] * (N+1)
    P = [0] * (N+1)
 
    for i in range(1,N+1):
        V[i], P[i] = map(int, input().split())
 
    dp = [[0] * (K+1) for _ in range(N+1)]
    # 열은 배낭의 크기
    # 행은 배낭에 i번째 물건이 있을 때의 가치 or 해당 배낭 크기 내의 최대 가치 
 
    for i in range(1, N+1):
        for j in range(1, K+1):
            if V[i] > j: # 배낭 크기j보다 부피V[i]가 커서 배낭에 넣을 수 없음
                dp[i][j] = dp[i-1][j] # 해당 배낭 크기 내의 최대 가치였던 윗줄 가치 입력
            else: # 배낭에 넣을 수 있음
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-V[i]] + P[i])
                # 부피가 꽉 차게(최대 가치가 되게) 넣을 거라 (배낭크기 - 지금부피)의 최대 가치에 지금 가치를 넣은 것과, 
                # 이미 해당 크기 내의 최대 가치였던 윗줄 가치 중에 더 큰 값을 입력
                 
    print(f'#{tc} {dp[N][K]}')