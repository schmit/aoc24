from solutions.io import lines

def get_value(matrix, loc):
    i, j = loc
    m = len(matrix)
    n = len(matrix[0])
    if i < 0: return None
    if j < 0: return None
    if i >= m: return None
    if j >= n: return None
    return matrix[i][j]

def scale_tuple(a, t):
    return tuple(a * v for v in t)

def add_tuples(x, y):
    return tuple(u + v for u, v in zip(x, y))

def one(matrix: list[str]):
    m = len(matrix)
    n = len(matrix[0])
    total = 0
    directions = [(di, dj) for di in (-1, 0, 1) for dj in (-1, 0, 1) if (di, dj) != (0, 0)]
    for i in range(m):
        for j in range(n):
            for d in directions:
                total += all(get_value(matrix, add_tuples((i, j), scale_tuple(a, d))) == ch 
                    for ch, a in zip('XMAS', range(4)))

    return total

def solve(input_file: str):
    matrix = list(lines(input_file))

    print(one(matrix))

