import sys

address_nums = [int(line.strip()) for line in sys.stdin.readlines()]

for address_num in address_nums:
    if address_num == 0:
        break
    else:
        width = 1
        for num in str(address_num):
            num = int(num)
            if num == 1:
                width += 2
            elif num == 0:
                width += 4
            else:
                width += 3
            width += 1
        print(width)