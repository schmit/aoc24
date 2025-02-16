from solutions.io import numbers


def check_sequence(seq, cond, default=True):
    if len(seq) <= 1:
        return default

    prev = seq[0]
    for val in seq[1:]:
        if not cond(val, prev):
            return False
        prev = val
    return True


def is_incr(seq):
    return check_sequence(seq, lambda cur, prev: cur >= prev)


def is_decr(seq):
    return check_sequence(seq, lambda cur, prev: cur <= prev)


def diff_between(seq, min_diff, max_diff):
    return check_sequence(
        seq, lambda cur, prev: min_diff <= abs(cur - prev) <= max_diff
    )


def is_safe(report):
    return (is_incr(report) or is_decr(report)) and diff_between(report, 1, 3)


def one(reports):
    return sum(1 for report in reports if is_safe(report))


def two(reports):
    n_safe = 0
    for report in reports:
        # brute force
        if is_safe(report) or any(
            is_safe([x for i, x in enumerate(report) if i != j])
            for j in range(len(report))
        ):
            n_safe += 1

    return n_safe


def solve(input_file: str):
    reports = list(numbers(input_file))
    print(one(reports))
    print(two(reports))
