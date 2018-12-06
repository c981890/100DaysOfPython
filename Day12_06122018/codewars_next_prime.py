# Get the next prime number!
# You will get a number n (>= 0) and your task is to find the next prime number.
# Make sure to optimize your code: there will numbers tested up to about 1012
# is_prime function from https://www.youtube.com/watch?v=2p3kwF04xcA

import time
import math

def is_prime_v3(n):
    """(int) -> bool
    Return "True" if 'n' is a prime number. False otherwise.
    >>>is_prime_v1(5)
    True
    >>>is_prime_v1(8)
    False
    """
    if n == 1:
        return False

    # If it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

def next_prime(n):
    """ (int) -> int
    Finds the next prime number.

    >>>next_prime(5)
    7
    >>>next_prime(12)
    13
    """
    m = n + 1
    while is_prime_v3(m) is False:
        m += 1
    return m

next_prime(0)

def is_prime_v1(n):
    """(int) -> bool
    Return "True" if 'n' is a prime number. False otherwise.
    >>>is_prime_v1(5)
    True
    >>>is_prime_v1(8)
    False
    """
    if n == 1:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False
    return True

# Time function
# t0 = time.time()
# for n in range(1, 100000):
#     is_prime_v1(n)
# t1 = time.time()
# print("Time required: ", t1 - t0)

def is_prime_v2(n):
    """(int) -> bool
    Return "True" if 'n' is a prime number. False otherwise.
    >>>is_prime_v1(5)
    True
    >>>is_prime_v1(8)
    False
    """
    if n == 1:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

# Time function
# t0 = time.time()
# for n in range(1, 100000):
#     is_prime_v2(n)
# t1 = time.time()
# print("Time required: ", t1 - t0)

def is_prime_v3(n):
    """(int) -> bool
    Return "True" if 'n' is a prime number. False otherwise.
    >>>is_prime_v1(5)
    True
    >>>is_prime_v1(8)
    False
    """
    if n == 1:
        return False

    # If it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

# Time function
# t0 = time.time()
# for n in range(1, 100000):
#     is_prime_v3(n)
# t1 = time.time()
# print("Time required: ", t1 - t0)
