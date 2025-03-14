def find_num(i,j,num):
    if len(num) == 7:
        result.add(num)
        return

    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni = i + di
        nj = j + dj

        if 0<=ni<N and 0<=nj<N:
            find_num(ni,nj,num+arr[ni][nj])

T = int(input())
N = 4
for tc in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]

    result = set()

    for i in range(N):
        for j in range(N):
            find_num(i,j,arr[i][j])

    print(f'#{tc} {len(result)}')