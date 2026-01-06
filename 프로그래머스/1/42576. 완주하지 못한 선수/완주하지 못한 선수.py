def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()
    N = len(participant)
    
    for i in range(N):
        if i == N-1:
            answer = participant[-1]
            break
            
        if participant[i] != completion[i]:
            answer = participant[i]
            break

    return answer