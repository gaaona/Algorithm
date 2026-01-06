def solution(board):
    N = len(board)
    answer = N * N
    
    di = [-1, 0, 1, -1, 1, -1, 0, 1]
    dj = [-1, -1, -1, 0, 0, 1, 1, 1]
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                answer -= 1
                for k in range(8):
                    ni = i + di[k]
                    nj = j + dj[k]

                    if 0<=ni<N and 0<=nj<N and board[ni][nj] == 0:
                        board[ni][nj] = -1
                        answer -= 1
    return answer