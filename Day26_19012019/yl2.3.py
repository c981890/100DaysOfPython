def voitis_nurkademangu(maatriks):
    i = 0
    if maatriks[0][0] == 'X':
        i += 1
    if maatriks[0][-1] == 'X':
        i += 1
    if maatriks[-1][0] == 'X':
        i += 1
    if maatriks[-1][-1] == 'X':
        i += 1
    return i == 4


def voitis_nurkademangu_2(tabel):
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            if (i == 0 or i == len(tabel)-1) and (j == 0 or j == len(tabel[i])-1):
                print(tabel[i][j])


def x_peadiagonaalil(maatriks):
    x = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            if i == j and maatriks[i][j] == 'X':
                x += 1
    return x


def x_korvaldiagonaalil(maatriks):
    x = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            if i == len(maatriks) - j - 1 and maatriks[i][j] == 'X':
                x += 1
    return x


def voitis_diagonaalidemangu(maatriks):
    return x_peadiagonaalil(maatriks) == 5 and x_korvaldiagonaalil(maatriks) == 5


def voitis_taismangu(maatriks):
    x = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            if maatriks[i][j] == 'X':
                x += 1
    return x == 25
