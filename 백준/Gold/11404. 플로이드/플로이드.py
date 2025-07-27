import sys

INF = 100000 * 100000 + 1

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

matrix = [[INF] * N for _ in range(N)]

for i in range(N):
    matrix[i][i] = 0

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())

    if matrix[start-1][end-1] > cost:
        matrix[start-1][end-1] = cost

for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

for row in matrix:
    print(' '.join(['0' if x == INF else str(x) for x in row]))
