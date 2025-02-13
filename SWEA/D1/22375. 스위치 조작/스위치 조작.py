T = int(input())

def switch_lights(N, A, B): # Ai를 Bi로 만드는
    i = 0
    cnt = 0
    # 0번 인덱스부터 1:1 비교하는 함수
    while i < N:
        if A[i] == B[i]:
            i += 1
        else: # 다르면 거기부터 뒤에 다 뒤집기  & cnt += 1
            j = i
            cnt += 1
            while j <N:
                B[j] = 1 - B[j]
                j += 1
            i += 1 # 달랐던 인덱스 다음부터 다시 1:1 비교

    return cnt # 배열 끝나면 cnt 반환



for tc in range(1, T+1):
    N = int(input()) # 총 스위치 개수
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    
    result = switch_lights(N, Ai, Bi)

    print(f'#{tc} {result}')