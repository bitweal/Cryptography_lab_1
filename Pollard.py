import math

def func_x(x, n):
    return (x**2 + 1) % n

def pollard(n):

    x0 = 2
    x_j = x0
    d = 1
    
    while d == 1:
        x_j = func_x(x_j, n)
        x_k = func_x(x_j, n)
        #print(x_k, '-', x_j)
        d = math.gcd((x_k - x_j), n)
    
    if d == n:
        return n
    else:
        return d