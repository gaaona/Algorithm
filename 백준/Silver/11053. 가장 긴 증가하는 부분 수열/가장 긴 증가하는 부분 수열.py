import sys

def find_max(i):
    cnt = 1
    for j in range(i+1,N):
        if nums[i] < nums[j]:
            cnt = max(cnt, 1 + ans[j])
    return cnt

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

ans = [0] * N
ans[-1] = 1

for i in range(N-2, -1, -1):
    ans[i] = find_max(i)

print(max(ans))
