def step_range(start, end, step):
    while start <= end:
        yield start
        start += step