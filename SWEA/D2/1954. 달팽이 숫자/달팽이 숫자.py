T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    i = j = 0
    dir = 0
    
    for num in range(1, N*N+1):
        arr[i][j] = num
        ni, nj = i + di[dir], j + dj[dir]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            dir = (dir+1) % 4
            i, j = i + di[dir], j + dj[dir]
	
    print(f'#{tc}')
    for row in arr:
        print(*row)