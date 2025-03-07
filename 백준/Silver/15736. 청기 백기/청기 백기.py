import sys
import math

N = int(input())

# 1부터 N 중에서 어떤 수의 제곱수의 경우에만 마지막까지 1로 남는다!!
# N 이하의 제곱수의 개수는 N의 루트의 정수 부분 만큼

result = int(math.sqrt(N))

print(result)
