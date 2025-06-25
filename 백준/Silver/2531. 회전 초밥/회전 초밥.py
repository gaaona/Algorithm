import sys

N, d, k, c = map(int, sys.stdin.readline().split())
dishes = [int(sys.stdin.readline()) for _ in range(N)]

# 원형 벨트 처리
dishes += dishes[:k-1]

count = [0] * (d + 1)
unique = 0

# 초기 윈도우 세팅
for i in range(k):
    if count[dishes[i]] == 0:
        unique += 1
    count[dishes[i]] += 1

# 쿠폰 초밥 처리
ans = unique + (0 if count[c] else 1)

# 슬라이딩 윈도우
for i in range(1, N):
    # 왼쪽 초밥 제거
    left = dishes[i - 1]
    count[left] -= 1
    if count[left] == 0:
        unique -= 1

    # 오른쪽 초밥 추가
    right = dishes[i + k - 1]
    if count[right] == 0:
        unique += 1
    count[right] += 1

    # 쿠폰 초밥 포함 여부
    temp = unique + (0 if count[c] else 1)
    if temp > ans:
        ans = temp

print(ans)
