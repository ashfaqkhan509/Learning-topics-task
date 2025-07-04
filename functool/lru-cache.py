import time
from functools import lru_cache


def fibonancy(n):
    if n < 2:
        return n
    return fibonancy(n-1) + fibonancy(n-2)

start = time.time()
fibonancy(20)
end = time.time()

print(f"{fibonancy.__name__} function take {(end-start) * 1000}ms during execution without cache.")


@lru_cache(maxsize=None)
def fibonancy(n):
    if n < 2:
        return n
    return fibonancy(n-1) + fibonancy(n-2)

start = time.time()
fibonancy(20)
end = time.time()

print(f"{fibonancy.__name__} function take {(end-start) * 1000}ms during execution with cache.")