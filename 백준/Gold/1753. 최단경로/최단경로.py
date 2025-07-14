import sys
import heapq

INF = 3000001

def shortest(start_node):
    global visited

    visited[start_node] = 0
    heap = []
    heapq.heappush(heap,(0, start_node))
    cnt = 0

    while heap:
        weight, goal = heapq.heappop(heap)
        if visited[goal] < weight:
            continue

        for w, next_node in graph[goal]:
            next_weight = weight + w

            if next_weight < visited[next_node]:
                visited[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))


V, E = map(int,sys.stdin.readline().split()) # 정점/간선
K = int(sys.stdin.readline()) # 시작 정점

graph = [[] for _ in range(V+1)]
visited = [INF] * (V + 1)

for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((w,v))

shortest(K)

for i in range(1, V+1):
    if visited[i] == INF:
        print("INF")
    else:
        print(visited[i])