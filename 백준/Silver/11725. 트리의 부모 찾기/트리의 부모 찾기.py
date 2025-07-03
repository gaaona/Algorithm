from collections import deque
import sys

N = int(input())
parent = [-1] * (N + 1)
left_child = [-1] * (N + 1)
right_child = [-1] * (N + 1)
nodes = [[] for _ in range(N + 1)]

q = deque()

for _ in range(N-1):
    node1, node2 = map(int, sys.stdin.readline().split())
    nodes[node1].append(node2)
    nodes[node2].append(node1)

parent[1] = 1
q.append(1)

while q:
    parent_node = q.popleft()
    for tmp in nodes[parent_node]:
        if parent[tmp] == -1:
            parent[tmp] = parent_node
            q.append(tmp)

for i in range(2,N+1):
    print(parent[i])
