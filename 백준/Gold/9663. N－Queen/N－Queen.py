import sys

def nqueens(row):
    global ans
    if row == N:
        ans += 1
        return
    
    for col in range(N):
        if not check_col[col] and not check_d1[row+col] and not check_d2[row-col+N-1]:
            check_col[col] = check_d1[row+col] = check_d2[row-col+N-1] = True
            nqueens(row + 1)
            check_col[col] = check_d1[row+col] = check_d2[row-col+N-1] = False

            
N = int(sys.stdin.readline())
ans = 0

check_col = [False] * N # 사용된 열인지 확인
check_d1 = [False] * (2 * N-1) # 사용된 대각선인지 확인
check_d2 = [False] * (2 * N-1) # 사용된 대각선인지 확인

nqueens(0)
print(ans)
