import sys

N = int(sys.stdin.readline().strip())
L = sys.stdin.readline().strip()

ans = 0
for i in range(N):
    tmp = (ord(L[i])-96) * (31 ** i)
    ans += tmp
    
print(ans)