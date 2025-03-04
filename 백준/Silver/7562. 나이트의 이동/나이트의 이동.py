import sys

def count_goal(gi, gj):
    global visited, q
    if (si, sj) == (gi, gj):
        return 0

    di = [-2, -1, 1, 2, 2, 1, -1, -2]
    dj = [1, 2, 2, 1, -1, -2, -2, -1]

    while q:
        i, j = q.pop(0)
        if (i, j) == (gi, gj):
            return visited[i][j] - 1

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return -1

T = int(sys.stdin.readline())

for tc in range(1, T + 1):
    N = int(sys.stdin.readline())
    sj, si = map(int, sys.stdin.readline().split())
    gj, gi = map(int, sys.stdin.readline().split())

    q = [(si, sj)]
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1

    ans = count_goal(gi, gj)
    print(ans)