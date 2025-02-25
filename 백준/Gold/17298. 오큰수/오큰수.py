import sys

T = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1] * T  # 기본값 -1로 초기화

for i in range(T):
    while stack and arr[stack[-1]] < arr[i]:  # 스택의 top보다 큰 수를 찾으면
        result[stack.pop()] = arr[i]  # 해당 위치에 오큰수 저장
    stack.append(i)  # 현재 인덱스를 스택에 push

print(*result)