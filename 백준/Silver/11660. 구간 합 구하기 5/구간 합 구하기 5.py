import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

S = [[0]*(N+1) for _ in range(N+1)]# 누적합 배열
for i in range(1, N+1):
    for j in range(1, N+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + matrix[i-1][j-1]
        # 누적합 = 같은 열 앞에 거 + 같은 행 위에 거 - 중첩된 값 + 입력 받은 값

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    print(ans)