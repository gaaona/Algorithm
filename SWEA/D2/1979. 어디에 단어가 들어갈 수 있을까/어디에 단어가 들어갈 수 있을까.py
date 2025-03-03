def check(i,j):
    cnt=0
    for x in range(K):
        if lst[i][j+x] ==1:
            cnt+=1
    if cnt==K and ((j+K-1)==N-1 or lst[i][j+K]==0):
        return 1
    else:
        return 0



testcase = int(input())
for tc in range(1,testcase+1):
    N, K = map(int,input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for _ in range(2):
        # print(lst)
        for i in range(N):
            for j in range(N-K+1):
                if lst[i][j] ==1 and (j==0 or lst[i][j-1]==0):
                    # check 시작
                    answer+=check(i,j)

        lst=list(map(list, zip(*lst)))

    print(f'#{tc} {answer}')