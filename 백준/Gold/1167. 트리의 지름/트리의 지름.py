def iterative_dfs(start):
    visited = [False] * (V+1)
    stack = [(start, 0)]
    max_dist, max_node = 0, start
  
    while stack:
        node, dist = stack.pop()
      
        if visited[node]:
            continue
          
        visited[node] = True
      
        if dist > max_dist:
            max_dist = dist
            max_node = node
          
        for nxt, nxt_d in graph[node]:
            if not visited[nxt]:
                stack.append((nxt, dist + nxt_d))
              
    return max_dist, max_node

V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    arr = list(map(int, input().split()))
  
    for i in range(1, len(arr)-1, 2):
        graph[arr[0]].append((arr[i], arr[i+1]))

_, farthest = iterative_dfs(1)
max_dist, _ = iterative_dfs(farthest)

print(max_dist)
