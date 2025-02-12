def find_palindrome(M, arr, N=8):
    cnt = 0
    
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
            else:
                cnt += 1
                
    return cnt

for test_case in range(1,11):
    M = int(input())
    rows = [input() for _ in range(8)]
    cols = [''] * 8

    for i in range(8):
        for c in range(8):
            cols[i] += rows[c][i]
    
    r_cnt = find_palindrome(M, rows)
    c_cnt = find_palindrome(M, cols)
    
    print(f'#{test_case} {r_cnt + c_cnt}')