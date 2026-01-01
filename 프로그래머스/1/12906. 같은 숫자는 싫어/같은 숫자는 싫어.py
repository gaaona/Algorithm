def solution(arr):
    answer = []
    N = len(arr)
    answer.append(arr[0])
    
    for i in range(1, N):
        if arr[i-1] == arr[i]:
            continue
        answer.append(arr[i])
        
    
    return answer