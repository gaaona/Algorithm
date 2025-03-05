import sys
from collections import deque

C = int(sys.stdin.readline())
N = int(sys.stdin.readline())

que = deque()
visited = [0] * (C+1)
routes = [[] for _ in range(C+1)]

for _ in range(N):
    n, c = map(int, sys.stdin.readline().split())

    routes[n].append(c)
    routes[c].append(n)

que.append(1)
visited[1] = 1

while que:
    t = que.popleft()
    for x in routes[t]:
        if not visited[x]:
            que.append(x)
            visited[x] = 1

print(visited.count(1)-1)