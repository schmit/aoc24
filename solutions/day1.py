from solutions.utils import lines

import collections


def parse(lines):
    for line in lines:
        number_strs = line.strip().split()
        yield [int(n) for n in number_strs]


def one(parsed_lines):
    first, second = zip(*parsed_lines)
    total_distance = 0
    for x, y in zip(sorted(first), sorted(second)):
        distance = abs(x-y)
        total_distance += distance

    return total_distance

def two(parsed_lines):
    first, second = zip(*parsed_lines)

    second_counts = collections.Counter(second)

    total = 0
    for n in first:
        total += n * second_counts[n]

    return total

def solve(input_file: str):
    parsed = list(parse(lines(input_file)))

    print("part 1:")
    print(one(parsed))

    print("part 2:")
    print(two(parsed))
