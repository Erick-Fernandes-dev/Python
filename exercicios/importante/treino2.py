contador = 1
fim = 5
acumulador = 0

while contador <= fim:
    x = int(input("Digite um valor: "))
    acumulador = acumulador + x
    contador = contador + 1
    acumulador += 1
    print("o valor da soma é:", acumulador)
