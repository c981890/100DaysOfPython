def on_rahulik(arvamus1, arvamus2, erinevus):
#    if abs(arvamus1 - arvamus2) < erinevus:
#        print(arvamus1, arvamus2, abs(arvamus1 - arvamus2))
#        print("True")
#        return False
    return abs(arvamus1 - arvamus2) <= erinevus or arvamus1 * arvamus2 >= 0


def dissonantside_arv(arvamused, lubatud_erinevus):
    dissonantsid = 0
    for i in range(len(arvamused) - 1):
        # print(arvamused[i], arvamused[i+1])
        if on_rahulik(arvamused[i], arvamused[i+1], lubatud_erinevus) is False:
            dissonantsid += 1
    return dissonantsid


print(dissonantside_arv([1, 4], 2))
print("---")
print(dissonantside_arv([-1, 3], 4))
print("---")
print(dissonantside_arv([1, 4, 0, -10, -1, 3, 42], 2))
print("---")
print(dissonantside_arv([1, -3, 1, 0, 0, -2, -3, 3, -3, 12], 3))
