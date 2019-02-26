def kysimused():
    print("OODATAV ELUIGA")
    while (True):
        print("Tee oma valik:")
        print("[1] Teie oodatav eluiga")
        print("[2] Milline oleks olnud teie oodatav eluiga olnud aastatel")
        print("[3] Naiste ja meeste oodatav eluiga graafikul")
        print("[q] Soovite lõpetada ja programmi sulgeda")
        print("> ", end = '')
        vastus = input()
        kasud(vastus)
        break


def kasud(vastus):
    for symbol in vastus:
        if vastus == 'q':
            break
        elif vastus == '1':
            oodatav_eluiga()


def oodatav_eluiga():
    print("Teie sugu:")
    print("[n] Naine")
    print("[m] Mees")
    sugu = input("> ")
    print("Teie vanus:")
    vanus = input("> ")
    sonastik_mehed = faili_sisselugemine("RV045 - RV045.csv")
    print(sonastik_mehed[vanus][-1])


def faili_sisselugemine(failinimi):
    fail = open(failinimi, encoding="UTF-8")
    sonastik = {}
    next(fail)
    for rida in fail:
        osad = rida.strip('\n').split(',', 1)
        sonastik[osad[0]] = osad[1]
    fail.close()
    return sonastik


kysimused()
