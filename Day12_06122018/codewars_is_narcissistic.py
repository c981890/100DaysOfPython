# A Narcissistic Number is a number of length n in which the sum of its digits
# to the power of n is equal to the original number. If this seems confusing,
# refer to the example below.
# Ex: 153, where n = 3 (number of digits in 153)
# 13 + 53 + 33 = 153

def is_narcissistic(i):
    """ (i) -> bool
    Returns whether or not i is a Narcissistic Number.
    >>>is_narcissistic(153)
    True
    >>>is_narcissistic(11)
    False
    """

    sum = 0
    for k in str(i):
        sum += int(k)**len(str(i))
    return i == sum

# shorter version
# return sum([int(n)**len(str(i)) for n in str(i)])==i
