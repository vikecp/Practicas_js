#p1
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n*n for n in valores]

#p2
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n%2 == 0]
print(valores_pares)

#p3
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(grados-32)*(5/9) for grados in temperatura_fahrenheit]

