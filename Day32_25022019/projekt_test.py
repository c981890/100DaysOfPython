import pandas as pd
import matplotlib.pyplot as plot


def graafik(failinimi):
    andmed = pd.read_csv(failinimi, delimiter=';')
    # andmed = andmed.set_index(' ')
    vanus = 1
    # indexNamesArr = andmed.index.values
    # print(indexNamesArr)

    sonastik = {}

    for x in range(101):
        sonastik[x] = "Vanus " + str(x)

    # print(sonastik)
    print(andmed.head(4))
    andmed.rename(index=sonastik, inplace=True)
    # print(andmed.columns)
    andmed.pop(' .1')
    # andmed = andmed.set_index(' ')
    print(andmed.head(4))

    # for i in range(len(indexNamesArr)):
    #     indexNamesArr[i] = "Vanus " + str(i)

    # print(andmed.columns[2:])
    # print("index ", andmed.index[39].values)
    # andmed.plot(andmed.index[39], andmed.columns.values)
    andmed.to_csv('RV045s_mehed_uus.csv', sep=';')
    # transponeeritud_andmed = andmed.T
    # print(transponeeritud_andmed.head(4))
    # transponeeritud_andmed["Vanus " + str(vanus)].plot()
    # plot.show()


graafik("RV045s_mehed.csv")
