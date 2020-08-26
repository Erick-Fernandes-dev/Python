contador = 1
fim = 5
acumulador = 1

while contador <= fim:
    acumulador = acumulador * contador

    print("contador", contador, "acumulador", acumulador,)

    contador = contador + 1

print("o valor do fatorial é:", acumulador)
