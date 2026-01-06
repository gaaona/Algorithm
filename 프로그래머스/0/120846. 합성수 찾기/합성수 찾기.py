def solution(n):
    answer = 0
    for i in range(4, n + 1):
        # 약수가 하나라도 존재하면 (합성수라면) 카운트
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                answer += 1
                break
    return answer