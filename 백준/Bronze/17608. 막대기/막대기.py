import sys

N = int(sys.stdin.readline())
sticks = [0] * (N +1) # 추후 계산을 위해 N+1 크기로 만듦

for i in range(1, N+1):
    sticks[i] = int(sys.stdin.readline()) # 입력값 넣기

    if sticks[i-1] < sticks[i]: # i-1(뒤의 막대)번째가 i번째보다 작아서 안보이는 경우ㅜ
        sticks[i-1] = 0 #



cnt = 1 # 맨 오른쪽(last)는 항상 보임
k = N # 보이는 순서대로 할 것임
last = sticks[-1]
max_h = sticks[-1]

while 0<k: # 0번 인덱스는 원래 비어있는 인덱스
    if sticks[k] > last and sticks[k] > max_h:
        cnt += 1
        if max_h < sticks[k]:
            max_h = sticks[k]
    k -= 1

print(cnt)