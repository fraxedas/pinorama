def step_range(start, end, step):
    while start <= end:
        yield start
        start += step

def name(prefix, pan, tilt):
    return str(prefix)  + "-" + str(pan) + "-" + str(tilt) + ".jpg"