def rek_fun(n):
    if n > 0:
        print("Põhi!")
    else:
        print(n)
        rek_fun(n + 2)


rek_fun(-7)
