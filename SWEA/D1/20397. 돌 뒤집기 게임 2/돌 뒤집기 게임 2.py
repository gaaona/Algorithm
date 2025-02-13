def reverse_pair_rocks(p1): # 0을 1로, 1을 0으로
    r1 = p1 ^ 1

    return r1


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    # N개의 돌, M번 뒤집는다
    arr = list(map(int, input().split()))

    for m in range(M):
        I, J = map(int, input().split())
        # i번째 돌을 사이에 두고 마주보는 j개의 돌  jjj i jjj
        # print(arr)

        i = I-1
        j = 1
        while i-j > -1 and i+j < N and j <= J: # 돌범위 내에서만 반복
            # print(arr[i-j], arr[i+j])
            if arr[i-j] == arr[i+j]:
                # print(i, j, arr)
                arr[i-j] = arr[i+j] = reverse_pair_rocks(arr[i-j])
                # print(arr[i - j], arr[i + j])
            # print(I,J, arr)
            j += 1

    print(f'#{test_case}', *arr)