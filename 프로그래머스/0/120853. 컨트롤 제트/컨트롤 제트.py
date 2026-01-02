def solution(s):
    answer = 0

    arr = s.split()
    N = len(arr)
    
    for i in range(N):
        if arr[i] == 'Z':
            answer -= int(arr[i-1])
        else:
            answer += int(arr[i])
    
    return answer