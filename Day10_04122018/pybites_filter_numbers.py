def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""

    return [nr for nr in numbers if nr > 0 and nr % 2 == 0]

filter_positive_even_numbers([-1, 0, 3, 4])
