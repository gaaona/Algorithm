def bfs(N, maze):
    visited = [[0] * N for _ in range(N)]
    q = [[1, 1]]
    visited[1][1] = 1

    while q:
        ti, tj = q.pop(0)

        for di, dj in [[0,1], [1,0],[0,-1],[-1,0]]:
            ni = ti + di
            nj = tj + dj

            while 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj]==0:
                if maze[ni][nj] == 3:
                    return 1
                else: # 0 통로 인 경우
                    q.append([ni, nj])
                    visited[ni][nj] = visited[ti][tj] + 1
    return 0

N = 16
T = 10

for testcase in range(1, T+1):
    tc = input()
    maze = [list(map(int, input())) for _ in range(N)]

    ans = bfs(N, maze)

    print(f'#{tc} {ans}')

