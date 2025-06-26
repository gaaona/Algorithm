N = int(input())
nums = list(map(int, input().split()))

arr = sorted(list(set(nums)))

dic = {arr[i] : i for i in range(len(arr))}

for j in nums:
    print(dic[j], end=" ")