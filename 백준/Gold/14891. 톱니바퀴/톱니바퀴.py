"""
톱니 1~4번
K번 회전 (시계or 반시계 방향)
맞닿은 부분 극 다르면 전파 아니면 전파안됨


"""


# 입력 1~4번 톱니 상태 12시부터 시계방향 N=0, S=1
wheels = ['']
twelve = [0] * 5
twelve[0] = -1

for i in range(1,5):
    state = input()
    wheels.append(state)

# 입력 회전 횟수 K
K = int(input())

# 회전 방법 번호,방향 시계=1, 반시계=-1
for _ in range(K):
    wheel_num, direction = map(int, input().split())

    rotate_dir = [0] * 5
    rotate_dir[wheel_num] = direction

    # 왼쪽 전파
    for x in range(wheel_num, 1, -1): # 기준바퀴랑 그 왼쪽(-1)바퀴 비교
        if wheels[x][(twelve[x]+6)%8] != wheels[x-1][(twelve[x-1]+2)%8]:
            rotate_dir[x-1] = -rotate_dir[x]
        else:
            break

    # 오른쪽 전파
    for y in range(wheel_num, 4): # 기준바퀴랑 그 오른쪽(+1) 바퀴 비교
        if wheels[y][(twelve[y]+2)%8] != wheels[y+1][(twelve[y+1]+6)%8]:
            rotate_dir[y+1] = -rotate_dir[y]
        else:
            break

    for z in range(1, 5): # 시계면 -1 반시계면 +1
        twelve[z] = (twelve[z] - rotate_dir[z]) % 8

# 점수 1번부터 12시 방향이 N=0, S=2**(번호-1)
answer = 0
for i in range(1, 5):
    if wheels[i][twelve[i]] == '1':
        answer += (2 ** (i-1))

print(answer)