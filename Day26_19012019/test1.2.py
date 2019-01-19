def fun(jar, i, j):
    if i < len(jar) and j < len(jar[i]):
        return jar[i][j]
    else:
        return 0


jarjend = [[1, 3, 4], [2, -5, 7]]

print(fun(jarjend, 0, 0), end=' ')
print(fun(jarjend, 2, 0), end=' ')
print(fun(jarjend, 0, 3))
