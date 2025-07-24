import sys

S1 = sys.stdin.readline().strip()
S2 = sys.stdin.readline().strip()

N, M  = len(S1), len(S2)

matrix = [[0]*(N+1) for _ in range(M)]

for i in range(M):
    for j in range(N):
        if S1[j] == S2[i]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j],  matrix[i][j-1])

print(matrix[M-1][N-1])