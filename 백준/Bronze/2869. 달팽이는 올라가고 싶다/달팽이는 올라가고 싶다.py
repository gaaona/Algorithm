import sys

A, B, V = map(int, sys.stdin.readline().split())

if (V-B) % (A-B) == 0 : # 올라가야 하는 높이(낮에 정상 도착)를 움직일 수 있는 높이 로 나눴을 때 딱 나눠짐
    print((V-B) // (A-B)) # 당일에 올라갈 수 있음
else:
    print((V-B) // (A-B) + 1) #그 다음 날에 가능