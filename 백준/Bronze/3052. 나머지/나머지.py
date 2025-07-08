import sys

ans = dict()
cnt = 0 # 나머지 종류 세는 변수

for _ in range(10):
    num = int(sys.stdin.readline())
    tmp = ans.setdefault(num%42, cnt) # setdefault는 key가 없으면 value까지 추가. 있으면 해당 값 반환

    if tmp == cnt: # 반환 값이 현재 센 수와 같으면
        cnt += 1

print(cnt)