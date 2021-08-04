import random

a = random.sample(range(100), 7)
b = random.sample(range(100), 10)

d = list(set(a))
e = list(set(b))
c = []
print(d)
print(e)
for i in d:
    for j in e:
        if i == j:
            c.append(i)

print("Primer Lista generada aleatoriamente sin duplicados: \n ", d)
print("Segunda Lista generada aleatoriamente duplicados:\n ", e)
print("Los elementos comunes en las dos listas son: \n ", c)