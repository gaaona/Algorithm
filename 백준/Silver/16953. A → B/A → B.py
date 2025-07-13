import sys

def cal(num, cnt):
    global ans

    if num > B: # 구해야하는 값보다 커지면 셀 필요 없음
        return
    
    if cnt > ans: # 최소 연산 값보다 커지면 셀 필요 없음
        return
    
    if num == B: # 구해야 하는 값이 나오면
        if ans > cnt: # 최소값인 경우
            ans = cnt
        return

    cal(num *2, cnt+1)
    cal((num * 10 + 1), cnt+1)


A, B = map(int, sys.stdin.readline().split())

ans = pow(10, 9)

cal(A, 1) # 조건에서 1을 더하라고 함

if ans == pow(10, 9):
    ans = -1

print(ans)