def factorization(num, i):
    while i <= num:
        if num == 1:
            break

        if num % i == 0:
            print(i)
            num //= i
        else:
            i += 1

N = int(input())

factorization(N,2)