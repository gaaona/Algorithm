import sys

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(i, j, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for d in range(4):
        ni, nj = i + di[d], j + dj[d]

        if 0 <= ni < R and 0 <= nj < C:
            alp_idx = ord(matrix[ni][nj]) - 65
            if not used[alp_idx]:
                used[alp_idx] = 1
                dfs(ni, nj, cnt + 1)
                used[alp_idx] = 0

R, C = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().strip()) for _ in range(R)]

used = [0] * 26
max_cnt = 0

start_alp = ord(matrix[0][0]) - 65
used[start_alp] = 1

dfs(0, 0, 1)
print(max_cnt)
