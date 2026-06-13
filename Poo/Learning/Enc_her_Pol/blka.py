num = [2,8,4,6,7,4,5]
pares = []


def par():
    for n in num:
        if n%2 == 0:
            pares.append(n)

par()
print(pares)