import sys

num = 0

for i in range(3):
    tmp = sys.stdin.readline().strip()

    if tmp.isdecimal(): # 확정 숫자가 나오면
        num = int(tmp)

        cnt = num + (3-i) # 입력 순서에 따라 다음 숫자 계산
        break


ans = ""

if cnt % 3 == 0:
    ans += "Fizz"

if cnt % 5 == 0:
    ans += "Buzz"

if ans == "":
    ans = cnt

print(ans)