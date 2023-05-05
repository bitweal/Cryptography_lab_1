import math
import numpy as np
import itertools

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

def col_xor(matrix, col1, col2):
    for i in range(len(matrix[0])):
        matrix[i][col2] = (matrix[i][col2] + matrix[i][col1]) % 2

    #for i in matrix:
        #print(i)
   # print('-'*25)
    return matrix

def simplify_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    determinate_rows = -1 #[False for _ in range(rows)]

    for j in range(cols):
        found_one = False
        for i in range(j, rows):
            if matrix[i][j] == 1:      
                found_one = True
                position_i = i
                break

        if found_one:
            for i in range(cols):
                if i != j and matrix[position_i][i] == 1: 
                    col_xor(matrix, j, i)

    for i in range(rows):
        count = 0
        for j in range(cols):
            if matrix[i][j] == 1:
                count += 1

        if count > 1:
            determinate_rows = i

    return matrix, determinate_rows

def find_zero_vectors(matrix, initial_vector):
    rows, cols = len(matrix), len(matrix[0])   
    result = [initial_vector]
    remember_one = []
    for i in range(cols):
        if matrix[initial_vector][i] == 1:
            remember_one.append(i)
    for j in remember_one:
        for i in range(rows):
            if i != initial_vector and len(result) <= len(remember_one) and matrix[i][j] == 1:
                result.append(i)


                
    return result

n = 2485021628404193
factor_base = build_factor_base(n)
print(factor_base)

smooth_numbers = find_smooth_numbers(n, factor_base)

#smooth_numbers = [[1,1,0,0], [1,1,0,1], [0,1,1,1], [0,0,1,0], [0,0,0,1]]

for i in smooth_numbers:
    print(i)

print('='*25)

matrix, determinate = simplify_matrix(smooth_numbers)

print('-'*25)

for i in matrix:
    print(i)

print('='*25)

if determinate != -1:
    print(find_zero_vectors(matrix, determinate))
else:
    matrix = np.array(matrix)
    indices = []

    for i in range(1, len(smooth_numbers) + 1):
        for combo in itertools.combinations(range(len(smooth_numbers)), i):
            if np.array_equal(np.sum(matrix[list(combo)], axis=0) % 2, np.zeros(len(smooth_numbers[0]), dtype=int)):
                indices.append(list(combo))
                
    print(indices)