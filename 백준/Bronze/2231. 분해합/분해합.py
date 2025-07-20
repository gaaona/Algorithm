import sys

N = int(sys.stdin.readline())

for num in range(max(0, N - 9 * len(str(N))), N):
    tmp = num # tmp값 초기화
    cnt = tmp # cnt 본체 값으로 초기화
    while tmp > 0: # //10 했을 때 0보다 큰 경우(최소 1의 자리수인 경우)
        cnt += tmp % 10
        tmp //= 10
    if cnt == N: # 분해합이 N과 일치하는 경우 
        print(num)
        break
else:
    print(0)
