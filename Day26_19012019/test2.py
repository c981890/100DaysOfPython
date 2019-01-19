a = [[1, 6, 7], [30, 21, 24], [44, 34, 45, 4], [46, 60, 52]]

s = a[0][0]
for rida in a:
    for el in rida:
        if el > s:
            s = el
print(s)

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] > s:
            s = a[i][j]
print(s)

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        if a[i][j] > s:
            s = a[i][j]
        j += 1
    i += 1
print(s)

i = 0
for i in range(len(a[0])):
    for j in range(len(a[i])):
        if (a[i][j] > s):
            s = a[i][j]
print(s)
