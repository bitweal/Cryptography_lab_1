import math

def find_result_x_y(factor_base, b, vectors, powers, n):
    print(factor_base)
    print(b)
    print(vectors)
    print(powers)
    print(n)
    for vector in vectors:
        i = 0
        x = 1
        y = 1
        for all_index in vector:
            x *= b[all_index]
            for p in range(len(powers[all_index])):
                if powers[all_index][p] != 0:
                    y *= factor_base[p]**powers[all_index][p]
        i += 1
        x = x % n
        y = int(math.sqrt(y) % n)
        first = math.gcd(x+y,n)
        second = math.gcd(x-y,n)
        print(first, second)
        if first > 1 and first < n and second > 1 and second < n:
              return first,second
    return 1


#factor_base = [-1,2,3,7,11,13]
#b = [95,286,381,1119,2619]
#vectors = [[0,4]]
#powers = [[1,4,1,0,0,0],[],[],[], [1,0,3,0,0,0]]
#n = 9073

#print(find_result_x_y(factor_base, b, vectors, powers, n))