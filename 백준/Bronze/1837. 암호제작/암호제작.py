def is_divided_under(num1, num2):
    for i in range(2, num2+1):
        if i == num2:
            return f'GOOD'
        if num1%i == 0:
            return f'BAD {i}'

code, r = map(int, input().split())
print(is_divided_under(code, r))