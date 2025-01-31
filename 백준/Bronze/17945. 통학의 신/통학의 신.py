a, b = map(int, input().split())

roots = []

priminary = -a
secondary = (a**2 - b)**(1/2)

for i in range(0, 3, 2):
    num = priminary + secondary * (i - 1)
    num = int(num)
    roots.append(num)
    
roots.sort()

if roots[0] == roots[1]:
	print(roots[0])
else:
    print(f'{roots[0]} {roots[1]}')