def solution(people, limit):
    N = len(people)
    answer = N
    
    people.sort()
    
    i, j = 0, N-1
    
    while i<j:
        if people[i] + people[j] <= limit:
            answer -= 1
            i += 1
            j -= 1
        else:
            j -= 1
    
        
    
    return answer