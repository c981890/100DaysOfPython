def zero_fuel(distance_to_pump, mpg, fuel_left):
    """(int, int, int) -> bool
    Tells you if it is possible to get to the pump or not.

    >>>zero_fuel(50, 25, 2)
    True
    >>>zero_fuel(100, 50, 1)
    False
    """

    return distance_to_pump / mpg <= fuel_left

zero_fuel(50, 25, 2)
zero_fuel(100, 50, 1)
