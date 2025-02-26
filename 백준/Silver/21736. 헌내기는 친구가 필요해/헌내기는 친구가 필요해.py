import sys
from collections import deque

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
campus = [sys.stdin.readline().strip() for _ in range(N)]

# 방문 배열
visited = [[False] * M for _ in range(N)]
q = deque()

# 'I' 위치 찾기
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            q.append((i, j))
            visited[i][j] = True
            break
    if q:
        break

# BFS 탐색 시작
cnt = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위

while q:
    ti, tj = q.popleft()

    for di, dj in directions:
        ni, nj = ti + di, tj + dj

        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            if campus[ni][nj] != 'X':  # 벽이 아닐 때만 이동 가능
                visited[ni][nj] = True
                q.append((ni, nj))
                if campus[ni][nj] == 'P':  # 사람이 있을 경우
                    cnt += 1

# 결과 출력
print(cnt if cnt else "TT")
