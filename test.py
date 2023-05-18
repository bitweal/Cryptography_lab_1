import random

# Miller Rabin
def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def miller_rabin(n, k):
    if n <= 2:
        return True
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for i in range(k):
        a = random.randint(2, n - 1)
        if euclidean_algorithm(a, n) != 1:
            return False
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Algorithm 2

def factorize(n):
    factors = []
    i = 2
    while i * i <= n and i <= 47:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    #if n > 1:
    #    factors.append(n)
    return factors

#print(factorize(9073))