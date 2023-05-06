import math
from Brillhart_Morrison import create_vectors

def find_result_x_y(factor_base, b, vectors, powers, n):
    for vector in vectors:
        i = 0
        x = 1
        y = 1
        for all_index in vector:
            x *= b[all_index]
            for p in range(len(powers[all_index])):
                if powers[all_index][p] != 0:
                    y *= factor_base[p]**powers[all_index][p]
                    print('y:', y)
                    #print('factor_base:', factor_base[p], 'power: ',powers[all_index][p])
        i += 1
        x = x % n
        print(y)
        y = int(math.sqrt(y) % n)
        first = math.gcd(x+y,n)
        second = math.gcd(x-y,n)
        if first > 1 and first < n and second > 1 and second < n:
              return first,second  
    return 0

try:
    factor_base, b, vectors, power, n = create_vectors()
    #print(factor_base)
    print(b)
    print(vectors)
    #print(power)
    #print(n)
    print(find_result_x_y(factor_base, b, vectors, power, n))  
except TypeError:
    print('I could not find solutions')