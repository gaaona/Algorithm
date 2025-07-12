S = input()
result = [-1] * 26  # 알파벳 개수만큼 -1로 초기화

for i in range(len(S)):
    idx = ord(S[i]) - ord('a')  # 알파벳 위치 계산
    if result[idx] == -1:       # 처음 등장한 경우만 기록
        result[idx] = i

for n in result:
    print(n, end=' ')
