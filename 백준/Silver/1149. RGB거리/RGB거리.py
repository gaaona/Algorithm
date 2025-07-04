import sys

N = int(sys.stdin.readline().rstrip())
prices = [0] * (N+1) 

for i in range(1,N+1):
    r, g, b = map(int, sys.stdin.readline().split())
    prices[i] = (r, g, b)

matrix = [[0] * 3 for _ in range(N+1)]

for i in range(3):
    matrix[1][i] = prices[1][i]

for i in range(1, N+1):
    matrix[i][0] = min(matrix[i-1][1], matrix[i-1][2]) + prices[i][0]

for i in range(1, N+1):
    for j in range(3):
        matrix[i][j%3] = min(matrix[i-1][(j+1)%3], matrix[i-1][(j+2)%3]) + prices[i][j]
        
print(min(matrix[N]))