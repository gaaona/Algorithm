# 5줄로 점수를 입력 받음
# 40 미만은 40으로 계산해서 평균 리턴

# 입력 받기 for _ in range(5)
# for i : 0->4 if 40 미만이면 a[i] = 40 바꾸고 총합에 += a[i]
# 5로 나눈 값 출력

nums = [int(input()) for _ in range(5)]
total = 0

for i in range(5):
    if nums[i] < 40:
        nums[i] = 40
    total += nums[i]

print(total//5)