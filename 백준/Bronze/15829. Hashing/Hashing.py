import sys

N = int(sys.stdin.readline().strip())
L = sys.stdin.readline().strip()

M = 1234567891
r = 31
ans = 0
power = 1

for i in range(N):
    num = ord(L[i]) - 96 # 'a': 97 -> 1
    ans = (ans + num * power) % M
    power = (power * r) % M

print(ans)