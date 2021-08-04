a = [1, 2, 2, 4, 5, 8, 11, 20, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

d = list(set(a))
e = list(set(b))
c = []

for i in d:
    for j in e:
        if i==j:
            c.append(i)

print("Primer Lista sin duplicados: \n ", d)
print("Segunda Lista duplicados:\n ", e)
print("Los elementos comunes en las dos listas son: \n ", c)