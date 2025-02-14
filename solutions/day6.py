from enum import Enum 
from collections import namedtuple

from solutions.utils import lines


Direction = Enum('Direction', 'UP DOWN LEFT RIGHT')
State = namedtuple('State', 'location direction')


def find_starting_position(situation: list[str]):
    for i in range(len(situation)):
        for j in range(len(situation[0])):
            if situation[i][j] == '^':
                return i, j

def forward(current: State):
    i, j = current.location
    match current.direction:
        case Direction.UP:
            return i - 1, j
        case Direction.DOWN:
            return i + 1, j
        case Direction.LEFT:
            return i, j - 1
        case Direction.RIGHT:
            return i, j + 1

def rotate(current: State):
    match current.direction:
        case Direction.UP:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.LEFT
        case Direction.LEFT:
            return Direction.UP

def step(situation: list[str], current: State):
    while True:
        i, j = forward(current)
        try:
            match situation[i][j]:
                case '.':
                    return State((i, j), current.direction)
                case '^':
                    return State((i, j), current.direction)
                case '#':
                    current = State(current.location, rotate(current))
        except IndexError:
            # we are out of bounds
            return None

def trace_path(situation, current: State):
    visited = set()

    while current:
        visited.add(current.location)
        current = step(situation, current)

    return visited



def one(situation: list[str]):
    start = State(find_starting_position(situation), Direction.UP)
    path = trace_path(situation, start)
    return len(path)


def solve(input_file: str):
    situation = list(lines(input_file))
    print(one(situation))
