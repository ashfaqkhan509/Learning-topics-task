from functools import partial

def power(a, b):
    return a**b

pow_of_2 = partial(power, b=2)
pow_of_5 = partial(power, b=5)
pow_of_10 = partial(power, b=10)

print(pow_of_2(5))