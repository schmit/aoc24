

def lines(input_path):
    with open(input_path, 'r') as f:
        for line in f:
            yield line
