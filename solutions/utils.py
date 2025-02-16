import time


def timeit(func):
    def timed(*args, **kwargs):
        start = time.process_time()
        result = func(*args, **kwargs)
        end = time.process_time()
        print(f"{func.__name__} took {end - start} seconds")
        return result

    return timed
