"""Public docstring."""

# 1. True
print("1. ", True and True)

# 2. False
print("2. ", False and True)

# 3. False
print("3. ", 1 == 1 and 2 == 1)

# 4. True
print("4. ", "test" == "test")

# 5. True
print("5. ", 1 == 1 or 2 != 1)

# 6. True
print("6. ", True and 1 == 1)

# 7. False
print("7. ", False and 0 != 0)

# 8. True
print("8. ", True or 1 == 1)

# 9. False
print("9. ", "test" == "testing")

# 10. False
print("10. ", 1 != 0 and 2 == 1)

# 11. True
print("11. ", "test" != "testing")

# 12. False
print("12. ", "test" == 1)

# 13. True
print("13. ", not (True and False))

# 14. False
print("14. ", not (1 == 1 and 0 != 1))

# 15. False
print("15. ", not (10 == 1 or 1000 == 1000))

# 16. False
print("16. ", not (1 != 10 or 3 == 4))

# 17. True
print("17. ", not ("testing" == "testing" and "Zed" == "Cool Guy"))

# 18. True
print("18. ", 1 == 1 and not ("testing" == 1 or 1 == 0))

# 19. False
print("19. ", "chunky" == "bacon" and not (3 == 4 or 3 == 3))

# 20. False
print("20. ", 3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))
