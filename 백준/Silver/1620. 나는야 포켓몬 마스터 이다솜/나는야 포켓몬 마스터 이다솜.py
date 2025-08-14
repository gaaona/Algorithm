import sys

n, m = map(int, sys.stdin.readline().split())

number_to_name = {}
name_to_number = {}

# 도감 채우기
for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    number_to_name[i] = name
    name_to_number[name] = i

# 문제 풀이
for _ in range(m):
    query = sys.stdin.readline().rstrip()
    if query.isdigit():
        print(number_to_name[int(query)])
    else:
        print(name_to_number[query])
