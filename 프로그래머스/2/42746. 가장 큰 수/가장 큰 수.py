def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 3, reverse=True)
    # 3번씩 반복하면 붙였을때 큰수 찾기 가능

    answer = str(int("".join(numbers)))
    
    return answer