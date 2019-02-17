def pikim_pikkus_rek3(struktuur):
    if (not isinstance(struktuur, list)):
        return 0
    jarjend = len(struktuur)
    for element in struktuur:
        pikim_jarjend = pikim_pikkus_rek3(element)
        if jarjend < pikim_jarjend:
            jarjend = pikim_jarjend
    return jarjend


print(pikim_pikkus_rek3([[[1, 2, 3]]]))







def pikim_pikkus_rek2(struktuur):
    pikim_jarjend = struktuur
    for element in struktuur:
        if (isinstance(element, list)):
            pikim_pikkus_rek2(element)
            if len(element) > len(pikim_jarjend):
                pikim_jarjend = element

    return len(pikim_jarjend)


print(pikim_pikkus_rek2([[[1, 2, 3]]]))


def pikim_pikkus_for_loop(struktuur):
    """
    (list) -> int.
    Võtab argumendiks suvalise sügavusega järjendi ja tagastab selles
    leiduva kõige pikema järjendi pikkuse.

    >>> pikim_pikkus(
        [[],[3,[4, 5], [2, 3, 4, 5, 3, 3], [7], 5, [1, 2, 3], [3, 4]],
        [1, 2, 3, 4, 5]]
        )
    7
    """
    pikim_jarjend = struktuur
    for member in struktuur:
        if len(member) > len(pikim_jarjend):
            pikim_jarjend = member
    return len(pikim_jarjend)


print(pikim_pikkus_for_loop([[[1, 2, 3]]]))


def pikim_pikkus_rek(struktuur):
    pikim_jarjend = struktuur
    for element in struktuur:
        if (isinstance(element, list)):
            if len(element) > len(pikim_jarjend):
                pikim_jarjend = element
            else:
                pikim_pikkus_rek(element)
    return len(pikim_jarjend)


print(pikim_pikkus_rek([[[1, 2, 3]]]))
