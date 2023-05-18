import math

def func_x(x, n):
    return (x**2 + 1) % n

def pollard(n):
    if n % 2 == 0:
        return 2

    x_j = 2
    x_k = x_j
    d = 1
    
    while d == 1:
        x_j = func_x(x_j, n)
        x_k = func_x(func_x(x_k, n),n)
        d = math.gcd((x_j - x_k), n)
    
    if d == n:
        return n
    else:
        return d