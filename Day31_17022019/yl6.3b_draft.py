def kes_on(arv, jarj):
    if len(jarj) == 0:
        return None
    if jarj[0][0] == arv:
        return jarj[0][1]
    return kes_on(arv, jarj[1:])


print(kes_on(54125632, [(4710209, 'Ernst'), (54125632, 'Uno'), (65242506, 'Arvo')]))
print(kes_on(5107261, [(4710209, 'Ernst'), (6524256, 'Arvo')]))
