
def read(input_path):
    with open(input_path, 'r') as f:
        return f.read().strip()

def lines(input_path):
    with open(input_path, 'r') as f:
        for line in f:
            yield line

def numbers(input_path):
    for line in lines(input_path):
        number_strs = line.strip().split()
        yield [int(n) for n in number_strs]
