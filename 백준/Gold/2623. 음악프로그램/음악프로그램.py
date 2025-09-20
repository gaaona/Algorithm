import sys

input = sys.stdin.readline


N, M = map(int, input().split())

routes = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
result = []

for _ in range(M):
    arr = list(map(int, input().split()))

    for i in range(1, arr[0]):
        routes[arr[i]].append(arr[i+1])
        degrees[arr[i+1]] += 1

q = []
for i in range(1, N+1):
    if degrees[i] == 0:
        q.append(i)

while q:
    now = q.pop(0)
    result.append(now)

    for route in routes[now]:
        degrees[route] -= 1
        if degrees[route] == 0:
            q.append(route)

if len(result) == N:
    for x in result:
        print(x)
else:
    print(0)
