# Prints positional arguments

def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25)

# Prints named arguments


def f(*args, **kwargs):
    print("Named:", kwargs)


f(galleons=100, sickles=50, knuts=25)


# def print(*object, sep=" ", end="\n", ...):
# print(*objects, sep=' ', end='\n', file=None, flush=False)
    # for object in objects:
