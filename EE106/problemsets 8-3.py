import math

def factgamma(x):
    result = 1
    while x>1:
        x-=1
        result *= x

    if abs(x-0.5)<1e-9:
        result *= math.sqrt(math.pi)
    elif abs(x - 1.0)<1e-9:
        result *= 1

    return result

x = float(input('enter an integer:\n'))

gamma_function = factgamma(x)

print(gamma_function)

    