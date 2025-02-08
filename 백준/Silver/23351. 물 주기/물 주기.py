from textwrap import indent
N, K, A, B = map(int, input().split())

arr = [K] * N
RIP = 0


valid = True
while valid:

    # 편의상 물부터 주기
    for i in range(A):
        index = int(i + (RIP % (N / A)) * A) % N
        arr[index] += B
    RIP += 1


    # 1 증발
    for j in range(N):
        arr[j] -= 1
        
        if arr[j] == 0:
            valid = False
            print(RIP)
            break
