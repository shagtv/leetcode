# fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, ...
from timeit import default_timer
from functools import cache


@cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


start = default_timer()
print(fib(33))
print(default_timer() - start)