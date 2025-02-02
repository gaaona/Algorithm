import sys

inputs = [int(line.strip()) for line in sys.stdin.readlines()]

cute_counts = 0
not_cute_counts = 0

for n in inputs[1:]:
    if n == 1:
        cute_counts += 1
    elif n == 0:
        not_cute_counts += 1

if cute_counts > not_cute_counts:
    print('Junhee is cute!')
elif cute_counts < not_cute_counts:
    print('Junhee is not cute!')