acumulador = 1
preco = 1
custo = int(input("Digite um valor: "))

while preco <= custo:
    preco = float(input("Digite o preço do produto comprado: "))

    acumulador = acumulador + preco
    preco = preco + 1
    acumulador = acumulador + 1 
    

print("Tamanho do estrago: ", acumulador)
