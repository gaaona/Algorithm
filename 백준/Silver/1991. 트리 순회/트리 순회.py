import sys

def pre_order(node):
    if node == -1:
        return
    print(chr(node+65), end='')
    pre_order(left[node])
    pre_order(right[node])

def mid_order(node):
    if node == -1:
        return
    mid_order(left[node])
    print(chr(node+65), end='')
    mid_order(right[node])

def post_order(node):
    if node == -1:
        return
    post_order(left[node])
    post_order(right[node])
    print(chr(node+65), end='')


alpha_to_num = dict()

for i in range(26):
    alpha_to_num.setdefault(i,chr(ord('A')+i))


N = int(sys.stdin.readline())
left = [-1] * 26
right = [-1] * 26

for i in range(N):
    p, l, r = sys.stdin.readline().split()

    if l != '.':
        left[ord(p)-65] = ord(l)-65

    if r != '.':
        right[ord(p)-65] = ord(r)-65


pre_order(0)
print()
mid_order(0)
print()
post_order(0)