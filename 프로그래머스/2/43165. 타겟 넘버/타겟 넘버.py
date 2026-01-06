answer = 0

def dfs(idx, numbers, target, summ):
    global answer
    
    N = len(numbers)
    
    if(idx== N and target == summ):
        answer += 1
        return
    if(idx == N):
        return

    dfs(idx+1,numbers,target,summ+numbers[idx])
    dfs(idx+1,numbers,target,summ-numbers[idx])
    
def solution(numbers, target):
    global answer
    
    dfs(0,numbers,target,0)
    
    return answer