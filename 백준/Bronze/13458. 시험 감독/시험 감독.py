import sys

test_rooms = int(sys.stdin.readline())
testers = list(map(int, sys.stdin.readline().split()))
supervisorA, supervisorB = map(int, sys.stdin.readline().split())

total = test_rooms

for tester in testers:
    if tester > supervisorA:
        remain = tester - supervisorA
        quotient = remain // supervisorB
        if remain % supervisorB != 0:
            quotient += 1
        total += quotient


print(total)
