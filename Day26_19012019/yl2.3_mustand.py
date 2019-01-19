bingo_tabel = [['X', 30, 34, 55, 'X'],
               [10, 'X', 40, 'X', 67],
               [5, 20, 'X', 48, 61],
               [4, 'X', 43, 'X', 70],
               ['X', 17, 33, 51, 'X'],
               ]


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


print(voitis_nurkademangu(bingo_tabel))


def x_peadiagonaalil(maatriks):
    x = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            if i == j and maatriks[i][j] == 'X':
                x += 1
    return x


print(x_peadiagonaalil(bingo_tabel))


def x_korvaldiagonaalil(maatriks):
    x = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            if i == len(maatriks) - j - 1 and maatriks[i][j] == 'X':
                x += 1
    return x


print(x_korvaldiagonaalil(bingo_tabel))


def voitis_diagonaalidemangu(maatriks):
    return x_peadiagonaalil(maatriks) == 5 and x_korvaldiagonaalil(maatriks) == 5


print(voitis_diagonaalidemangu(bingo_tabel))

def voitis_taismangu(maatriks):
    x = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            if maatriks[i][j] == 'X':
                x += 1
    return x == 25

print(voitis_taismangu(bingo_tabel))

'''
def loo_diagonaalmaatriks(jark, sisu):
    maatriks = []
    for i in range(jark):       # välimine tsükkel tekitab ridu
        rida = []
        for j in range(jark):   # sisemine hoolitseb veergude eest
            if i == j:          # tegemist on peadiagonaali elemendiga
                rida.append(sisu)
            else:
                rida.append(0)
        maatriks.append(rida)
    return maatriks
'''
