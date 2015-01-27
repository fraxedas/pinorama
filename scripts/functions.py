def step_range(start, end, step):
    while start <= end:
        yield start
        start += step

def name(prefix, pan, tilt):
    return prefix  + "-" + str(pan) + "-" + str(tilt) + ".jpg"