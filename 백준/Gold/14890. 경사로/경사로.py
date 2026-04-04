"""
한쪽끝에서 반대쪽 끝으로 = 길
경사로 높이는 1 길이는 L

"""
def check(line):
    is_laddered = [False] * N
    i = 0
    while i < N-1:
        # 경사로 놓을 수 있음? 중간부터 안 되면 바로 그 길은 끝임
        if line[i] == line[i+1]: # 높이 같으면 킵고잉
            i += 1
        elif line[i] - 1 == line[i+1]: # 내리막
            if i+L >= N: # L칸이 범위 내에 있음
                # print("범위X")
                return False

            for k in range(1, L+1): # 조건 탐색
                if is_laddered[i+k]:
                    # print("이미 경사로 놓음")
                    return False

                if line[i+1] != line[i+k]: # L개 연속된 칸 높이가 같음
                    # print("평평X")
                    return False
            else:
                for p in range(1, L+1): # 경사로 놓기
                    is_laddered[i+p] = True
                i += L
        elif line[i] + 1 == line[i+1]: # 오르막
            if i - (L-1) < 0:  # L칸이 범위 내에 있음
                # print("오 범위X")
                return False

            for k in range(L):  # 조건 탐색
                if is_laddered[i - k]: # 경사로 이미 놓음
                    # print("오 이미 경사로")
                    return False

                if line[i] != line[i - k]: # L개 연속된 칸 높이가 같음
                    # print("오 평평X")
                    return False
            else:
                for p in range(L): # 경사로 놓기
                    is_laddered[i - p] = True
                i += 1
        else:
            # print("조건 안됨 길 아님")
            return False
    return True # 이러면 네 하고 개수 세기


# 입력
N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 입력 끝

answer = 0
matrix_ = list(zip(*matrix)) # 가로세로 바꿈

# 지나기기 위한 조건
for j in range(N):
    is_checked = check(matrix[j])
    if is_checked:
        answer += 1

    is_checked = check(matrix_[j])
    if is_checked:
        answer += 1

print(answer)
