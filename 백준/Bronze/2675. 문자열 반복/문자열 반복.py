T = int(input())

for tc in range(T):
    times, text = input().split()
    times = int(times)
    P = ''

    for i in text:
        P += i * times 
        # print(txt)   
    print(P, end='')
    print() 