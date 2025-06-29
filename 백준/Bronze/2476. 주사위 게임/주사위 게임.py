N = int(input())
ans = 0

for _ in range(N):
    dices = list(map(int, input().split()))
    dices.sort() # 크기 순 정렬

    if dices[0] == dices[1] == dices[2]: # 셋 다 같은 경우
        cnt = 10000 + dices[0] * 1000
    elif dices[0] == dices[1] or dices[1] == dices[2]: # 두 개만 같은 경우
        cnt = 1000 + dices[1] * 100 # 중복되는 숫자는 가운데 숫자임
    else:
        cnt = dices[2] * 100 # 제일 큰 수는 2번 인덱스

    if ans < cnt: # 최고가 갱신
        ans = cnt

print(ans)