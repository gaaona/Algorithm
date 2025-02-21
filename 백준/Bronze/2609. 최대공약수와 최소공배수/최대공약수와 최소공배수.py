def factorization(num):
    if num == 1:
        return [1]
    factors = []
    i = 2
    while i * i <= num:
        if num % i: # 약수면
            i += 1 # 다음 숫자로
        else: # i가 num의 약수가 아니면
            num //= i # num은 i로 나눈 값
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

num1, num2 = map(int, input().split())
if num1 > num2:
    num1, num2 = num2, num1

if num1 == num2 or num2 % num1 == 0: # 두 수가 같거나 큰 수가 작은 수로 나눠지는 경우
    print(num1)  # 최대공약수
    print(num2)  # 최소공배수
else:
    A = factorization(num1)
    B = factorization(num2)

    # 최대공약수 구하기
    common_divisors = set(A) & set(B)
    common_divisor = 1
    for fac in common_divisors:
        common_divisor *= fac ** min(A.count(fac), B.count(fac))

    # 최소공배수 구하기
    common_multiples = set(A) | set(B)
    common_multiple = 1
    for fac in common_multiples:
        common_multiple *= fac ** max(A.count(fac), B.count(fac))

    print(common_divisor)
    print(common_multiple)
