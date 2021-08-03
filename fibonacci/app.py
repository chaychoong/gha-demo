import sys


def fibonacci(n):
    """Return the nth value in the fibonacci series."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(int(sys.argv(1))))
