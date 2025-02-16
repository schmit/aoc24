from solutions.io import numbers

import collections


def one(parsed_lines):
    first, second = zip(*parsed_lines)
    total_distance = 0
    for x, y in zip(sorted(first), sorted(second)):
        distance = abs(x - y)
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
    parsed = list(numbers(input_file))

    print("part 1:")
    print(one(parsed))

    print("part 2:")
    print(two(parsed))
