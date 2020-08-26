'''def soma(lista):
  soma = 0
  for elemento in lista:
    soma = soma + elemento
  print(soma)

lista1 = [2, 3, 4, 4]
lista2 = [9, 0, 8, 1]
lista3 = [23, 4, 0, 0]

soma(lista1)
soma(lista2)
soma(lista3)

print("OUTRA MANEIRA: RETURN")

def soma(lista):
  soma = 0 
  for elemento in lista:
    soma = soma + elemento
  
  return soma

lista = [8, 9, 9, 0]
lista0 = [2, 4, 5, 6, 4]
lista01 = [3, 4, 5, 6, 9]

resulatdo_1 = soma(lista)
resulatdo_2 = soma(lista0)
resulatdo_3 = soma(lista01)

print(resulatdo_1, resulatdo_2, resulatdo_3)

print("OUTRO PASSO.")

def somador(lista):
  somador = 0

  for elemento in lista:
    somador = somador + elemento
  return somador

lista_1 = [2, 3, 4, 5]
lista_2 = [4, 5, 6, 2]
lista_3 = [5, 6, 7, 9]

print(somador(lista_1) + somador(lista_2) + somador(lista_3))
'''
def somador(lista):
  somando = 0

  for elemento in lista:
    somando += elemento
  return somando

lista1 = [2, 4, 5]
lista2 = [3, 7, 9]
lista3 = [10, 12, 14]

print(somador(lista1) + somador(lista2) + somador(lista3))

print(somador(lista1))
print(somador(lista2))
print(somador(lista3))

def calcule():
  n1 = int(input("Digite um valor: "))
  n2 = int(input("Digite mais um valor: "))
  soma = n1 + n2
  return soma

print(calcule())





