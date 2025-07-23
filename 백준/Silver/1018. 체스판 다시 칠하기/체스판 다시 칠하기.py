import sys

M, N = map(int, sys.stdin.readline().split())
board = []
min_count = 64 # 8*8

for i in range(M):
    line = sys.stdin.readline().rstrip()
    num_row = []
    
    for j in range(N):
        if line[j] == "B":
            num_row.append(0)
        else:
            num_row.append(1)
    board.append(num_row)


for i in range(M-7):
    for j in range(N-7):
        count1 = 0  # 첫 칸이 0(흑) 기준
        count2 = 0  # 첫 칸이 1(백) 기준
        
        for x in range(8):
            for y in range(8):
                # 실제 보드
                val = board[i + x][j + y]
                # 기준 판과 비교(흑,백)
                if (x + y) % 2 == 0: # x랑 y가 다를 때만 == 0
                    if val != 0: count1 += 1
                    if val != 1: count2 += 1
                else:
                    if val != 1: count1 += 1
                    if val != 0: count2 += 1
        min_count = min(min_count, count1, count2) # 현재 최소값/흑시작 계산값/백시작 계산값 중 최소값
print(min_count)