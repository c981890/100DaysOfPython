def rek_fun(n):
    if n > 0:
        print("Põhi!")
    else:
        print(n)
        rek_fun(n + 2)


rek_fun(-7)


def print_alla(n):
    if n <= 0:
        print("Stop!")
    else:
        print(n)
        print_alla(n - 1)


print_alla(4)


def print_ules(n):
    if n <= 0:
        print("Stop!")
    else:
        print_ules(n-1)
        print(n)


print_ules(4)


def print_alla_ules(n):
    if n <= 0:
        print("Stop!")
    else:
        print(n)
        print_alla_ules(n - 1)
        print(n)


print_alla_ules(4)
