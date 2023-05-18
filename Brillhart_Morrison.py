import math
import time
from Brillhart_Morrison_search_solutions import find_result_x_y

def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("The function {} was executed in {:.2f} seconds".format(func.__name__, execution_time))
        return result
    return wrapper

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

def build_factor_base(n, a):
    L = int(math.exp(math.sqrt(math.log(n) * math.log(math.log(n))))**a)
    primes = []
    for p in range(2, L):
        if is_prime(p) and legendre_symbol(n, p) == 1:
            primes.append(p)
    factor_base = [-1] + primes
    return factor_base

def is_smooth(num, factor_base):
    smooth_number = []
    power = []
    for p in factor_base:
        count = 0
        if num < 0:
            num *= -1
            count += 1
            power.append(1)
            smooth_number.append(1)
            continue
        elif num >= 0 and p == -1:
            power.append(0)
            smooth_number.append(0)
            continue
        while num % p == 0:
            num //= p        
            count += 1
        power.append(count)
        smooth_number.append(count % 2)
    return smooth_number, power


def find_smooth_numbers(n, factor_base):
    a = [int(math.sqrt(n))]
    v = [1]
    u = [a[0]]
    pre_b, b = 0, 1
    smooth_numbers = []
    remember_b = []
    power = []
    powers_smooth_number = []
    for i in range(1, len(factor_base) + 1):
        v.append((n - u[i - 1]**2) // v[i - 1])
        a.append(int((math.sqrt(n) + u[i - 1]) // v[i]))
        u.append(a[i] * v[i] - u[i - 1])
        pre_b, b = b, (a[i-1]*b + pre_b) % n
        prepare = b**2 % n
        if prepare >= n // 2:
            prepare -= n
        remember_b.append(b)
        smooth, powers_smooth_number = is_smooth(prepare,factor_base)
        smooth_numbers.append(smooth)
        power.append(powers_smooth_number)
    return remember_b, smooth_numbers, power

def col_xor(matrix, col1, col2):
    for i in range(len(matrix)):
        matrix[i][col2] = (matrix[i][col2] + matrix[i][col1]) % 2
    return matrix

def simplify_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    undeterminate = []
    for j in range(cols):
        found_one = False
        for i in range(rows):
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
            undeterminate.append(i)
    return matrix, undeterminate

def find_zero_vectors(matrix, undeterminate, base, bi, powers, n):
    cols = len(matrix[0])  
    for index in undeterminate:   
        result = []
        remember_one = []
        for i in range(cols):
            if matrix[index][i] == 1:
                remember_one.append(i)
        result.append([index])
        for j in remember_one:
            combo = []
            for i in range(index+1):
                if i in undeterminate and undeterminate[i] == True:  
                    continue
                if i != index and matrix[i][j] == 1:
                    combo.append(i)      
                    break
            result.append(combo)
        undeterminate[index] = True
        combinations = generate_combinations(result)
        x_y = find_result_x_y(base, bi, combinations, powers, n)
        if x_y == 'no solutions':
            continue
        else:
            return x_y
    return -1

def generate_combinations(result):
    combinations = [[]]
    for vector_list in result:
        new_combinations = []
        for combination in combinations:
            for vector in vector_list:
                new_combinations.append(combination + [vector])
        combinations = new_combinations
    return combinations


def start(n ,a = 1 / math.sqrt(2)):
    factor_base = build_factor_base(n, a)
    b, smooth_numbers, powers = find_smooth_numbers(n, factor_base)
    matrix, undeterminate = simplify_matrix(smooth_numbers)
    dict_undeterminate = {}
    for number in undeterminate:
        dict_undeterminate[number] = False
    if dict_undeterminate:
        x_y = find_zero_vectors(matrix, dict_undeterminate, factor_base, b, powers, n)
        return x_y        
    else:
        return -1

@timeit_decorator
def brillhart_morrison(n,a=1 / math.sqrt(2)):
    while True:
        result = start(n,a)
        if result == -1:
            if a < 1.5:
                a += 0.1  
                print('a = ',a)
                continue
            answer = input("Do you want to increase a and try again? ")
            print('a = ',a)
            if  answer == 'No' or answer == 'no':
                print("goodbye")            
                return -1
            else:
                a += 0.1        
                continue
        else:
            #print(result)
            #x = input()
            return result

#n = int(input('Enter n: '))
#a = 1 / math.sqrt(2)
#print(brillhart_morrison(n,a))