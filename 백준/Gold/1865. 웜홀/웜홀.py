import sys

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    matrix = [[] for _ in range(N+1)]
  
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        matrix[S].append((E, T))
        matrix[E].append((S, T))   # 도로는 양방향
      
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        matrix[S].append((E, -T))  # 웜홀(음수)는 단방향

    # 가상노드(0)에서 모든 노드로 0 가중치 간선 추가
    dist = [10001] * (N+1)
    dist[0] = 0
  
    graph = [[] for _ in range(N+1)]
  
    for i in range(1, N+1):
        graph[0].append((i, 0))
      
    for v in range(1, N+1):
        for u, w in matrix[v]:
            graph[v].append((u, w))
          
    ans = "NO"
    for i in range(N):
        for v in range(N+1):
            for u, w in graph[v]:
                if dist[u] > dist[v] + w:
                    dist[u] = dist[v] + w
                    if i == N-1:
                        ans = "YES"
    print(ans)
