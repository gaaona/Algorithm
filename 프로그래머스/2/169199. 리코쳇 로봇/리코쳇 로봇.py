from collections import deque

def solution(board):
    N = len(board)
    M = len(board[0])
    
    di = [-1,1,0,0] # 상하좌우
    dj = [0,0,1,-1]
    
    q = deque()
    visited = [[False] * M for _ in range(N)]
    
    found_R = False
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                found_R = True
                q.append((i,j,0))
                visited[i][j] = True                
                break
        if found_R:
            break

    while q:
        i,j,cnt = q.popleft()
        
        if board[i][j] == "G":
            return cnt
        
        for d in range(4):
            ni,nj = i, j
            
            while True:
                ti,tj = ni + di[d], nj + dj[d]

                if not (0<=ti<N and 0<=tj<M):
                    break
                if board[ti][tj] == "D":
                    break
                
                ni,nj = ti,tj
            
            if not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni,nj, cnt +1))
                
                    
                
    
    return -1