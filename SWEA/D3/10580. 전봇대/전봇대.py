def count_intersections(A, B):
    N = len(A)
    cnt = 0

    for i in range(N):
        for j in range(i + 1, N):  # i와 j가 서로 다른 선분을 나타냄
            # 선분 i와 j가 교차하는지 확인
            if (A[i] < A[j] and B[i] > B[j]) or (A[i] > A[j] and B[i] < B[j]):
                cnt += 1

    return cnt


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = [0] * N
    B = [0] * N

    for i in range(N):
        A[i], B[i] = map(int, input().split())

    ans = count_intersections(A, B)
    print(f'#{tc} {ans}')