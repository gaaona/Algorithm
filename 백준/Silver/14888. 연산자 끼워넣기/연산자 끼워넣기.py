import sys
import itertools

N = int(sys.stdin.readline())
oper_nums = list(map(int, sys.stdin.readline().split()))  # 숫자(순서 고정)

oper_dict = {0: '+', 1: '-', 2: '*', 3: '/'}
oper_counts = list(map(int, sys.stdin.readline().split()))  # 연산자들 각 개수(순서 변화 예정)

oper_str = ''  # 개수마다 시퀀스 연산자로 반복해서 str에 붙여줄 거임
for i in range(4):
    oper_str += (oper_dict[i] * oper_counts[i])

max_v = -1000000001 # 최소 -10억이라길래 -10억 1
min_v = 1000000001  # 최대 10억이라길래 10억 1

permutations = list(itertools.permutations(oper_str))
unique_perm = set(permutations) # 중복 제거

for p in unique_perm:
    # 숫자가 N개 연산자가 언제나 N-1개고 연산자 우선순위 없이 앞에서부터니까 퍼펙트 셔플 문제처럼 섞어줄 거
    cal = oper_nums[0]  # 첫 번째 숫자
    i = 0
    while i < len(p):  # p가 4개일지 3개일지 5개일지 몰라서 아무튼 arr는 len(p)+1임
        num1 = cal
        num2 = oper_nums[i + 1]  # 숫자 배열 arr가 인덱스가 하나 많음!

        if p[i] == '+':
            # print(f'{num1} + {num2}')
            cal = num1 + num2
        elif p[i] == '-':
            # print(f'{num1} - {num2}')
            cal = num1 - num2
        elif p[i] == '*':
            # print(f'{num1} * {num2}')
            cal = num1 * num2
        elif p[i] == '/':
            # print(f'{num1} // {num2}')
            if num1 < 0:  # 음수면 C++처럼 계산한다해서 그거 반영
                cal = -((-num1) // num2)
            else:
                cal = num1 // num2
        i += 1

    if max_v < cal:
        max_v = cal
    if min_v > cal:
        min_v = cal

print(max_v)
print(min_v)