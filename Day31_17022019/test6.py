from turtle import *


def sone_rek(sone):
    if len(sone) == 0:
        return ""
    else:
        return sone[-1] + sone_rek(sone[:-1])


print(sone_rek("suli"))



def tase_rek(tase):
    if tase == 0:
        print("Tase 0")
    else:
        tase_rek(tase - 1)
        print("Tase " + str(tase))


tase_rek(3)


def printKuhu(n):
    if n <= 0:
        print("Stop!")
    else:
        print(n - 1)
        printKuhu(n - 1)
        print(n)


print(printKuhu(2))


def printKuhu(n):
    if n >= 30:
        print("Stop!")
    else:
        print(n)
        printKuhu(n + 5)


print(printKuhu(5))


def hanoi(arv, lähe, siht, ajutine):
    if arv > 0:
        hanoi(arv - 1, lähe, ajutine, siht)
        print("Ketas liigutati platsilt " + str(lähe) + " platsile " + str(siht))
        hanoi(arv - 1, ajutine, siht, lähe)


hanoi(3, "A", "B", "C")


"""
def puu(pikkus):
    if pikkus < 5:
        forward(pikkus)
        back(pikkus)
    else:
        forward(pikkus)
        left(45)
        puu(0.6 * pikkus)
        right(90)
        puu(0.6 * pikkus)
        left(45)
        back(pikkus)


delay(0)
speed(10)
left(90)
puu(100)
"""
