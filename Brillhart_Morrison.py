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

def is_smooth(num, factor_base):
    smooth_number = []
    for p in factor_base:
        count = 0
        if num < 0:
            num *= -1
            count += 1
            smooth_number.append(1)
            continue
        elif num >= 0 and p == -1:
            smooth_number.append(0)
            continue
        while num % p == 0:
            num //= p        
            count += 1
        smooth_number.append(count % 2)
    return smooth_number

def find_smooth_numbers(n, factor_base):
    a = [int(math.sqrt(n))]
    v = [1]
    u = [a[0]]
    pre_b, b = 0, 1
    smooth_numbers = []
    for i in range(1, len(factor_base) + 1):
        v.append((n - u[i - 1]**2) // v[i - 1])
        a.append(int((math.sqrt(n) + u[i - 1]) // v[i]))
        u.append(a[i] * v[i] - u[i - 1])
        pre_b, b = b, (a[i-1]*b + pre_b) % n
        prepare = b**2 % n
        if prepare >= n // 2:
            prepare -= n
        smooth_numbers.append(is_smooth(prepare,factor_base))

    return smooth_numbers

n = 9073
factor_base = build_factor_base(n)
print(factor_base)

smooth_numbers = find_smooth_numbers(n, factor_base)
print(smooth_numbers)