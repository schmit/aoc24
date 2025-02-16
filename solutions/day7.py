from collections import namedtuple
from operator import add, mul

from solutions.io import lines
from solutions.utils import timeit

Equation = namedtuple("Equation", "value terms")


def first(xs):
    return xs[0]


def second(xs):
    return xs[1]


def parse_line(line: str) -> Equation:
    v_str, terms_str = line.split(": ")
    value = int(v_str)
    terms = [int(x) for x in terms_str.split()]
    return Equation(value, terms)


def can_solve_eqn(equation, operators):
    # recursively solve by trying all operators
    n_terms = len(equation.terms)
    if n_terms == 1:
        return equation.value == first(equation.terms)

    x, y = first(equation.terms), second(equation.terms)
    rest = equation.terms[2:]
    return any(
        can_solve_eqn(Equation(equation.value, [op(x, y), *rest]), operators)
        for op in operators
    )


@timeit
def one(equations: list[Equation]):
    return sum(eqn.value for eqn in equations if can_solve_eqn(eqn, [add, mul]))


def concat(x, y):
    return int(str(x) + str(y))


@timeit
def two(equations: list[Equation]):
    return sum(eqn.value for eqn in equations if can_solve_eqn(eqn, [add, mul, concat]))


def solve(input_file: str):
    equations = [parse_line(line) for line in lines(input_file)]
    print(one(equations))
    print(two(equations))
