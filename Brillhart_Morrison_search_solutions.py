import math

def find_result_x_y(factor_base, b, vectors, powers, n): 
    for vector in vectors: 
        x = 1
        y = 1
        for all_index in vector:
            x *= b[all_index]
            for p in range(len(powers[all_index])):
                if powers[all_index][p] != 0:
                    y *= factor_base[p]**powers[all_index][p]      
        x = x % n
        y = int(math.sqrt(y) % n)
        first = math.gcd(x+y,n)
        second = math.gcd(x-y,n)
        if first > 1 and first < n and second > 1 and second < n and first != second:
            return first,second
    return 'no solutions'