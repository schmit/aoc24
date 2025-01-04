import re

from solutions.utils import read


def one(code):
    pattern = re.compile('mul\((\d+),(\d+)\)')
    matches = pattern.findall(code)
    return sum(int(x) * int(y) for x, y in matches)

def two(code):
    do_pattern = re.compile("do\(\)")
    dont_pattern = re.compile("don't\(\)")

    
    total = 0
    enabled = True
    while code:
        # find switch point
        match = dont_pattern.search(code) if enabled else do_pattern.search(code)
        if enabled:
            # if enabled, add values up to switch point
            if match:
                total += one(code[:match.start()])
            else:
                # end of string
                total += one(code)

        # proceed to next section (if exists)
        code = code[match.end():] if match else None
        enabled = not enabled
    
    return total

def solve(input_path):
    code = read(input_path)
    print(one(code))
    print(two(code))
