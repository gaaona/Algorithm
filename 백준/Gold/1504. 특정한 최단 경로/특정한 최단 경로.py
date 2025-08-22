import heapq
import sys

INF = 200000 * 1000 + 1

def dijkstra(start_node, end_node):
    distances = [INF] * (N + 1)
    distances[start_node] = 0

    q = [(0, start_node)]

    while q:
        dist, node = heapq.heappop(q)

        if dist > distances[node]:
            continue

        if node == end_node:
            return distances[node]

        for next_distance, next_node in routes[node]:
            new_distance = dist + next_distance

            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                heapq.heappush(q, (new_distance, next_node))

    return INF



N, E = map(int, sys.stdin.readline().split())
routes = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    routes[a].append((c, b))
    routes[b].append((c, a))

v1, v2 = map(int, sys.stdin.readline().split())

v1_first = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
v2_first = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if v1_first >= INF and v2_first >= INF:
    print(-1)
else:
    ans = v1_first
    if v1_first > v2_first:
        ans = v2_first
    print(ans)
