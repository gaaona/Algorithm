def gcd(A, B):
    while B:
        A, B = B, A % B
    return A

def lcm(A, B):
    return A * B // gcd(A, B)

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    if A > B:
        A, B = B, A
    print(lcm(A, B))
