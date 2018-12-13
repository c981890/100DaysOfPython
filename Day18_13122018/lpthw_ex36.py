"""LPTHW Exercise 36."""

from sys import exit


def take_it():
    """Take it function."""
    dead("Harry Potter finds you and chops your head  off.")


def leave_it():
    """Leave it function."""
    print("You run back and meet Professor McGonagall.")
    print("What do you do?")
    print("a) Insult her")
    print("b) Greet her")

    next = input("> ")

    if next == "a":
        dead("You have been expellled from life.")
    else:
        print("She greets you back and tells you to go back to class.\n"
              "You live happily ever after.")
        exit(0)


def destroy_it():
    """Destroy it function."""
    print("Magic power seeps out of the wand.")
    print("You absorb it.")
    print("What do you do next?")
    print("a) You go on a killing rampage")
    print("b) You decide you are not worthy of the power")

    next = input("> ")

    if next == "a":
        dead("The police finds you and locks you while you are working on "
             "decapitating your first victim.")
    elif next == "b":
        dead("You accidentally kill yourself while trying to discard the "
             "power.")
    else:
        print("Try again.")


def dead(why):
    """End of the game."""
    print(why, "Good job!")
    exit(0)


def start():
    """Start of function."""
    print("You find a magic wand.")
    print("What do you do?")
    print("a) Take it")
    print("b) Leave it")
    print("c) Destroy it")

    next = input("> ")

    if next == "a":
        take_it()
    elif next == "b":
        leave_it()
    elif next == "c":
        destroy_it()
    else:
        dead("You live happily ever after.")


start()
