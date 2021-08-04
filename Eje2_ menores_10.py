a = [1, 2, 3, 4, 5, 6, 10, 15, 20, 37, 7, 50, 9]
b = []
for i in a:
    if i < 10:
        b.append(i)

print("Los elementos de la lista menores a 10 son: \n ", b)
