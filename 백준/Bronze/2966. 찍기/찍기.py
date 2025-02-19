N = int(input())
answer_sheet = input()

name_dict = {'Adrian': 'ABC', 'Bruno': 'BABC', 'Goran': 'CCAABB'}

for x in name_dict:
    # print(name_dict[x])
    while True:
        name_dict[x] += name_dict[x]
        if len(name_dict[x]) >= N:
            break

max_cnt = 0
winner = []

for j in name_dict:
    cnt = 0
    # print(name_dict[j])
    # print(j)
    for i in range(N):
        if answer_sheet[i] == name_dict[j][i]:
            cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        winner = [j]

    elif max_cnt == cnt:
        winner.append(j)

print(max_cnt)
for k in winner:
    print(k)