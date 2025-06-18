import sys

N, M = map(int, sys.stdin.readline().split())

words = [sys.stdin.readline().rstrip() for _ in range(N)]

words.sort()
words.append('')

result = []
cnt = 1

for i in range(N):
    if len(words[i]) < M:
        continue

    if words[i] == words[i+1]:
        cnt += 1
    else:
        result.append((words[i], cnt, len(words[i])))
        cnt = 1

result.sort(key=lambda x:(-x[1], -x[2], x[0]))

for x in result:
    print(x[0])