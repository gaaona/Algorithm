def f(s, t):
    if len(s) == len(t):
        return s == t
    res = False
    if t[-1] == 'A':
        res |= f(s, t[:-1])
    if t[0] == 'B':
        res |= f(s, t[1:][::-1])  # t를 뒤집고 맨 뒤 B 제거
    return res

S = input().strip()
T = input().strip()

print(1 if f(S, T) is True else 0)
