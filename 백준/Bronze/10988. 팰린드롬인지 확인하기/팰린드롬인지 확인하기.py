txt = input()
N = len(txt)

paline = 1

i = 0
while i <N//2:
    if i == (N-1):
        break
    if txt[i] == txt[N-i-1]:
        i += 1
    else:
        paline = 0
        break

print(paline)