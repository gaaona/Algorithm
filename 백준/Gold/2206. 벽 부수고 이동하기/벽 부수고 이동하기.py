import sys
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
# visited[i][j][0] : 벽을 아직 안 부수고 방문
# visited[i][j][1] : 벽을 이미 부수고 방문

queue = deque()
queue.append((0, 0, 0))  # x, y, 벽을 부순 횟수 (0 or 1)
visited[0][0][0] = 1

while queue:
    i, j, broken = queue.popleft()
    
    if i == N-1 and j == M-1:
        print(visited[i][j][broken])
        break
        
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        
        if 0 <= ni < N and 0 <= nj < M:
            
            if matrix[ni][nj] == 0 and visited[ni][nj][broken] == 0: # 벽이 아니고 아직 방문 X
                visited[ni][nj][broken] = visited[i][j][broken] + 1
                queue.append((ni, nj, broken))
            elif matrix[ni][nj] == 1 and broken == 0 and visited[ni][nj][1] == 0: # 벽을 만났고, 아직 벽을 부술 수 있음
                visited[ni][nj][1] = visited[i][j][broken] + 1
                queue.append((ni, nj, 1))
else:
    print(-1)
