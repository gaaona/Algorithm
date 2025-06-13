def find_seen_number(N,multi,cnt):
    global nums

    if cnt == 10:
        print(N * (multi-1))
        return

    num = N * multi
    str_num = str(num)

    for x in str_num:
        idx = int(x)
        if nums[idx]:
            continue
        nums[idx] = True
        cnt += 1
    find_seen_number(N,multi+1,cnt)


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    nums = [False] * 10

    print(f'#{tc}', end=' ')
    find_seen_number(N, 1, 0)