T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int,input().split())
    arr = [0] * N

    for i in range(1, Q+1): # tc 안의 턴
        L, R = map(int, input().split())

        for j in range(L-1, R):
            arr[j] = i

    print(f'#{test_case}', *arr)