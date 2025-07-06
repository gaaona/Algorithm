import sys

N = int(sys.stdin.readline())
tri = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i+1):
        if j == 0: # 0번 인덱스면 j-1이 없어서 따로 처리
            tri[i][j] += tri[i-1][j]
        elif j == i: # i번 인덱스면 i-1이 없어서 따로 처리
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[-1]))