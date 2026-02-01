import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    
    while scoville:
        mini = heapq.heappop(scoville)
        
        if mini >=K:
            break
        
        if not scoville:
            answer = -1
            break
            
        second_mini = heapq.heappop(scoville)
        
        answer += 1
        heapq.heappush(scoville, mini+second_mini*2)
        
        
    
    return answer