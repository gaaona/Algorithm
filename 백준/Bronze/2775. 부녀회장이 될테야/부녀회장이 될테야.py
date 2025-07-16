import sys

T = int(sys.stdin.readline())

matrix = [[0] * 15 for _ in range(15)]

for i in range(15):
    for j in range(1, 15):
        if i == 0:
            matrix[i][j] = j
        else:
            matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

for t in range(T):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    print(matrix[K][N])
