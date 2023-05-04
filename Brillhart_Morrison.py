import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def legendre_symbol(a, p):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        if p % 8 == 1 or p % 8 == 7:
            return 1
        else:
            return -1
    elif a >= p:
        return legendre_symbol(a % p, p)
    elif a % 2 == 0:
        return legendre_symbol(2, p) * legendre_symbol(a // 2, p)
    else:
        if a % 4 == 3 and p % 4 == 3:
            return -1 * legendre_symbol(p, a)
        else:
            return legendre_symbol(p, a)

def build_factor_base(n):
    a = 1 / math.sqrt(2)
    L = int(math.exp(math.sqrt(math.log(n) * math.log(math.log(n))))**a)
    primes = []
    for p in range(2, L):
        if is_prime(p) and legendre_symbol(n, p) == 1:
            primes.append(p)
        if len(primes) >= 100:
            break
    factor_base = [-1] + primes
    return factor_base

n = 9073
factor_base = build_factor_base(n)
print(factor_base)