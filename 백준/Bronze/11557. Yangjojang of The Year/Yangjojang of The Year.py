T = int(input())

for i in range(T):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    for k in range(N):
        arr[k][1] = int(arr[k][1])

    max_uni = arr[0][0]
    max_drink = arr[0][1]
    for j in range(1, N):
        if max_drink < arr[j][1]:
            max_uni = arr[j][0]
            max_drink = arr[j][1]
    print(max_uni)
        