def mi_generador():
    for x in range(1, 5):
        yield x * 10



g = mi_generador()
print(next(g))


def generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

gene = generador()

print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))

