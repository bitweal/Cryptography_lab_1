import math

def func_x(x, n):
    x = x*x + 1 % n
    return x

def pollard(n):

    x0 = 1
    x_j = x0
    d = 1
    
    while d == 1:
        x_j = func_x(x_j, n)
        x_k = func_x(x_j, n)
        print(x_k, '-', x_j)
        d = math.gcd((x_k - x_j), n)
    
    if d == n:
        return n
    else:
        return d

n = int(input('Enter n: '))
print(pollard(n))