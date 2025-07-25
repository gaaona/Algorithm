import sys

N = int(sys.stdin.readline().strip())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, c, w = map(int, sys.stdin.readline().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

def dfs(start):
    visited = [False] * (N+1)
    stack = [(start, 0)]
    visited[start] = True
    
    max_dist = 0
    farthest = start

    while stack:
        node, cnt = stack.pop()
        if max_dist < cnt :
            max_dist = cnt
            farthest = node
        for nxt, weight in tree[node]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append((nxt, cnt + weight))
    return max_dist, farthest

_, far = dfs(1)
max_length, _ = dfs(far)
                    
print(max_length)