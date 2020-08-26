lista = []

for valor in range(0, 8):
  numero = int(input("Digite um valor: "))
  if valor == 0 or numero > lista[-1]:
    lista.append(numero)
  else:
    contador = 0
    while contador < len(lista):
      if numero <= lista[contador]:
        lista.insert(contador, numero)
        break

      contador = contador + 1

print("=" *30)
print(lista)
