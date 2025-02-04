import sys

for line in sys.stdin.readlines():
    amigo, amiga = map(int, line.split())
    if amigo and amiga:
        print(amigo + amiga)
    else:
        break