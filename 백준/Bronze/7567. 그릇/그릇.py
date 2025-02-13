bowls = input()
N = len(bowls)
height = 10

for i in range(1, N):
    if bowls[i-1] != bowls[i]:
        height += 10
    else:
        height += 5
print(height)