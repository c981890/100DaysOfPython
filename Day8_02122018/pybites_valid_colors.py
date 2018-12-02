VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        asked_color = input("Please enter a color: ")
        if asked_color.lower() == 'quit':
            print('bye')
            break
        elif asked_color.lower() in VALID_COLORS:
            print(asked_color.lower())
        else:
            print("Not a valid color")
        pass

print_colors()
