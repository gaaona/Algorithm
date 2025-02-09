def get_primes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    
    for i in range(2, limit):
        if sieve[i]:  
            primes.append(i)
            for j in range(i * i, limit, i):  
                sieve[j] = False
                
    return primes  

def is_divided_under(num1, num2):
    primes = get_primes(num2)  # K보다 작은 소수 리스트 생성
    for p in primes:
        if num1 % p == 0:
            return f'BAD {p}'
    return "GOOD"

code, r = map(int, input().split())
print(is_divided_under(code, r))
