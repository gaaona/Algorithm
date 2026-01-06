from collections import deque

def solution(numbers, target):
    answer = 0
    N = len(numbers)

    q = deque([(-1, 0)])
    
    while q:
        idx, summ = q.popleft()
        if idx == N-1:
            if summ == target:
                answer += 1
        else:
            q.append((idx+1,summ-numbers[idx+1]))
            q.append((idx+1,summ+numbers[idx+1]))
        
    return answer