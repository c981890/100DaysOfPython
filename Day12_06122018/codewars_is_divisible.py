def is_divisible(n, x, y):
    """ (int, int, int) -> bool
    Checks if a number n is divisible by two numbers x AND y.
    All inputs are positive, non-zero digits.

    >>>is_divisible(3, 1, 3)
    True
    >>>is_divisible(12, 2, 6)
    True
    >>>is_divisible(100, 5, 3)
    False
    >>>is_divisible(12, 7, 5)
    False
    """

    return n % x == 0 and n % y == 0

is_divisible(3, 1, 3)
is_divisible(100, 5, 3)
