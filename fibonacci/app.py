import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    """Return the nth value in the fibonacci series."""
    if type(n) != int:
        return None
    if n < 0:
        return None
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))
