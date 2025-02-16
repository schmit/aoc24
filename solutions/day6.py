from enum import Enum
from collections import namedtuple

from solutions.io import lines


Location = tuple
Direction = Enum("Direction", "UP DOWN LEFT RIGHT")
State = namedtuple("State", "location direction")


def find_starting_position(grid: list[str]):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                return i, j


def forward(current: State) -> Location:
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


def rotate(current: State) -> Direction:
    match current.direction:
        case Direction.UP:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.LEFT
        case Direction.LEFT:
            return Direction.UP


def is_in_bounds(grid, location):
    i, j = location
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def get_value(grid, location):
    if is_in_bounds(grid, location):
        i, j = location
        return grid[i][j]
    return None


def step(grid: list[str], current: State) -> State | None:
    while True:
        i, j = forward(current)
        match get_value(grid, (i, j)):
            case ".":
                return State((i, j), current.direction)
            case "^":
                return State((i, j), current.direction)
            case "#":
                current = State(current.location, rotate(current))
            case None:
                return None


def trace_path(grid, current: State):
    path = []

    while current:
        path.append(current)
        current = step(grid, current)

    return path


def does_path_cycle(grid, current: State):
    """
    Checks whether we are on a path that cycles.

    A path cycles if it hits a state that we have already visited.
    A path does not cycle if it goes out of bounds.
    """
    visited = set()
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = step(grid, current)

    return False


def copy_grid(grid):
    return [list(row) for row in grid]


def add_obstruction(grid, obstruction):
    new_grid = copy_grid(grid)
    i, j = obstruction
    new_grid[i][j] = "#"
    return new_grid


def one(grid: list[str]):
    start = State(find_starting_position(grid), Direction.UP)
    path = trace_path(grid, start)
    return len(set(state.location for state in path))


def two(grid: list[str]):
    start = State(find_starting_position(grid), Direction.UP)
    path = trace_path(grid, start)

    obstructions = set()
    for state in path:
        if state.location != start.location:
            grid_with_obstruction = add_obstruction(grid, state.location)
            if does_path_cycle(grid_with_obstruction, start):
                obstructions.add(state.location)

    return len(obstructions)


def solve(input_file: str):
    grid = [[ch for ch in line] for line in lines(input_file)]
    print(one(grid))
    print(two(grid))
