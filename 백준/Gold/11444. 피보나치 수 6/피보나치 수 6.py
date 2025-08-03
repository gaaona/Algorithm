def mul(A, B, MOD):
    return [
        [(A[0][0]*B[0][0]+A[0][1]*B[1][0])%MOD, (A[0][0]*B[0][1]+A[0][1]*B[1][1])%MOD],
        [(A[1][0]*B[0][0]+A[1][1]*B[1][0])%MOD, (A[1][0]*B[0][1]+A[1][1]*B[1][1])%MOD]
    ]

def mat_pow_iter(mat, n, MOD):
    result = [[1, 0], [0, 1]]  # 단위행렬
    base = mat

    while n > 0:
        if n % 2 == 1:
            result = mul(result, base, MOD)
        base = mul(base, base, MOD)
        n //= 2

    return result

N = int(input())
MOD = 1000000007

if N == 0:
    print(0)
else:
    F = [[1,1],[1,0]]
    res = mat_pow_iter(F, N-1, MOD)
    print(res[0][0])
