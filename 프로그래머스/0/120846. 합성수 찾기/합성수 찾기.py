dividers = [False] * 101

for i in range(4, 101):
    for j in range(2,i//2+1):
        if i%j==0:
            dividers[i] = True
            break
    


def solution(n):
    global dividers
    answer = 0
    
    for i in range(n+1):
        if dividers[i]:
            answer += 1
            
    return answer