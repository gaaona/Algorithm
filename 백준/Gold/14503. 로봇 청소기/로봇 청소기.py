"""
N*M 직사각형
각 칸은 벽 혹은 빈칸
청소기는 방향이 있고 동서남북 중 하나
각 칸의 좌표 (r,c) [(0,0) ~ (N-1, M-1)]
빈칸은 다 청소 x
"""

# 입력 방크기
N, M = map(int, input().split())

# 입력 칸 좌표 r,c 랑 방향 d
r, c, d = map(int, input().split())

# 방향은 [북, 동, 남, 서]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 지도 벽 만들기...
matrix = [[1] * (M+2)]

for i in range(N):
    matrix += [[1] + list(map(int, input().split())) + [1]]

matrix += [[1] * (M+2)]

# matrix[i][j]가 1이면 벽이고 0이면 빈칸
# 입력 끝


# 로직
not_cleaned = [[True] * (M+2) for _ in range(N+2)] # 이미 청소했는지 확인

# 좌표 조정(벽 만들었으니까)
r += 1
c += 1

is_finished = False # 루프 탈출
answer = 0

while not is_finished:
    if matrix[r][c] == 0 and not_cleaned[r][c]:# 현재칸이 청소되지 않은 경우
        not_cleaned[r][c] = False # 현재 칸 청소
        answer += 1

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈칸 있음?
    for i in range(4): # 있음
        d = (d-1)%4 # 반시계 방향을로 90도 회전
        ni = di[d] + r
        nj = dj[d] + c

        if matrix[ni][nj] == 0 and not_cleaned[ni][nj]:    # 현재 칸의 주변 4칸 중 청소되지 않은 빈칸 있음?
            r,c = ni, nj # 바라보는 방향 기준으로 앞이 청소되지 않은 빈칸의 경우 전진 후 반복
            break
    else: # 없음
        ni = di[(d+2)%4] + r
        nj = dj[(d+2)%4] + c

        if matrix[ni][nj] == 0: # 바라보는 방향 유지하고 한칸 후진 가능?
            r,c = ni, nj
            # 한칸 후진 후 반복
        else: # 벽인 경우
            is_finished = True
            # 작동 멈춤
            break


print(answer)