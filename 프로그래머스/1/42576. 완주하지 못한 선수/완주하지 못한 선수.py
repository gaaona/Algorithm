from collections import Counter

def solution(participant, completion):
    # 각 명단의 개수를 센 뒤 차집합을 구함
    answer = Counter(participant) - Counter(completion)
    
    # 결과는 {'mislav': 1} 형태이므로 key값만 추출
    return list(answer.keys())[0]