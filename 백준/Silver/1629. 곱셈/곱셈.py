import sys

def power_func(a,b,c): # A*B의 나머지나 (A의 나머지*B의 나머지)의 나머지 는 같음(모듈러 연산)
    if b == 0:
        return 1 # a의 0제곱은 1
    
    # 분할 정복
    cnt = power_func(a, b // 2, c) # 계속 지수를 절반씩 나눠서 연산해서 곱하기
    cnt = (cnt * cnt) % c # 짝수번 만큼 쪼개고 연산 후 최종으로 제곱해서 원복
    
    if b % 2 == 1: # b//2하기 때문에 홀수 인 경우 한 번 더 밑수를 곱하기
        cnt = (cnt * a) % c
    
    return cnt


A,B,C = map(int, sys.stdin.readline().split())

print(power_func(A,B,C))