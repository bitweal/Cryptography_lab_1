def find_zero_vectors(matrix, initial_vector):
    rows, cols = len(matrix), len(matrix[0])
    result = []
    remember_one = []
    for i in range(cols):
        if matrix[initial_vector][i] == 1:
            remember_one.append(i)

    result.append([initial_vector])
    for j in remember_one:
        combo = []
        for i in range(rows):
            if i != initial_vector and matrix[i][j] == 1:
                combo.append(i)
        result.append(combo)

    print(result)
    combinations = generate_combinations(result)
    print('result: ', combinations)
    return combinations


def generate_combinations(result):
    combinations = [[]]
    for vector_list in result:
        new_combinations = []
        for combination in combinations:
            for vector in vector_list:
                new_combinations.append(combination + [vector])
        combinations = new_combinations
    return combinations

matrix = [
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1]
]

#matrix = [[1,0,0,0],[0,0,0,1],[0,1,0,0],[0,0,1,0],[1,0,0,1]]
start_vector = 1

combinations = find_zero_vectors(matrix, start_vector)
print(combinations) 