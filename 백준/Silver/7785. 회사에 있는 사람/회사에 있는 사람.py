import sys

N = int(sys.stdin.readline())

inhouse = set()

for _ in range(N):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        inhouse.add(name)
    else:
        inhouse.remove(name)

for person in sorted(inhouse, reverse=True):
    print(person)