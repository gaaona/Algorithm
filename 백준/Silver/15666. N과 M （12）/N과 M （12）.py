import sys

def find(i, cnt):
    global path

    if cnt == M:
        print(*path)
        return

    prev = -1
    for j in range(i,N):
        if prev == nums[j]: # 중복 숫자 출력 방지
            continue

        path.append(nums[j])
        find(j, cnt+1)
        path.pop()
        prev = nums[j]



N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

path = []
find(0,0)