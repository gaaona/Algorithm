# import sys
#
# def bin_search(num):
#     start, end = 0, len(nums)
#     while start < end:
#         mid = (start + end) // 2
#         if nums[mid] < num:
#             start = mid + 1
#         else:
#             end = mid
#     return start
#
#
#
# N = int(sys.stdin.readline())
# nums = []
#
# for i in range(N):
#     num = int(input())
#     idx = bin_search(num)
#     nums.insert(idx, num)
#     print(nums[i//2])
# print('최종 정렬 리스트:', nums)

import heapq
import sys

N = int(sys.stdin.readline())
left = []
right = []

for _ in range(N):
    num =  int(sys.stdin.readline())

    if len(left) == len(right): # 왼쪽을 더 길게 하기 위해(//2를 구현)
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and -left[0] > right[0]:
        left_val = -heapq.heappop(left) # 왼쪽 중 제일 큰 값
        right_val = heapq.heappop(right) # 오른쪽 중 제일 작은 값
        heapq.heappush(left, -right_val)
        heapq.heappush(right, left_val)

    print(-left[0])
