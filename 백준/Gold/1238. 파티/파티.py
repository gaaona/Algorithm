import sys
import heapq

def dik(start_node):
    dist = [INF] * (N+1)
    dist[start_node] = 0
    q = []
    heapq.heappush(q,(0,start_node))

    while q:
        t, e = heapq.heappop(q)

        if dist[e] < t:
            continue

        for next_time, next_node in routes[e]:
            new_time = t + next_time

            if dist[next_node] > new_time:
                dist[next_node] = new_time
                heapq.heappush(q, (new_time, next_node))

    return dist


N, M, X = map(int, sys.stdin.readline().split())

INF = 10000 * 1000 +1

routes = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    routes[start].append((time, end))

ans = 0

to_X_dist = [0] * (N+1)

for i in range(1, N+1):
    if i == X:
        continue
    dist = dik(i)
    to_X_dist[i] = dist[X]

X_to_home_dist = dik(X)

dist = [to_X_dist[i] + X_to_home_dist[i] for i in range(1, N+1)]
print(max(dist))