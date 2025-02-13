import itertools as it
import functools as ft
from solutions.utils import lines


def create_rules(raw_rules):
    rules = {}
    for raw_rule in raw_rules:
        before, after = [int(x) for x in raw_rule.split('|')]
        if before < after:
            rules[(before, after)] = True
        else:
            rules[(after, before)] = False

    return rules

def correct_order(first, second, rules) -> bool:
    if first < second and not rules.get((first, second), True):
        return False
    if first > second and rules.get((second, first), False):
        return False
    return True


def parse(input_path):
    all_lines = lines(input_path)

    raw_rules = it.takewhile(lambda line: line != '', all_lines)
    rules = create_rules(raw_rules)
    pages = [[int(x) for x in line.split(',')] for line in all_lines]

    return rules, pages

def is_valid(seq, rules):
    for i, x in enumerate(seq):
        if not all(correct_order(x, y, rules) for y in seq[i+1:]):
            return False
    return True

def fix_order(seq, rules):
    return sorted(seq, key=ft.cmp_to_key(lambda x, y: -1 if correct_order(x, y, rules) else 1))

def one(rules, pages):
    return sum(seq[len(seq)//2] for seq in pages if is_valid(seq, rules))

def two(rules, pages):
    invalid_sequences = [seq for seq in pages if not is_valid(seq, rules)]
    return sum(fix_order(seq, rules)[len(seq)//2] for seq in invalid_sequences)
    
def solve(input_path):
    rules, pages = parse(input_path)
    print(one(rules, pages))
    print(two(rules, pages))
    
