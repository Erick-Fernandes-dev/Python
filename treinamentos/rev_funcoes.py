def repetir(x, y):
  somador = 0 
  lista = []
  while somador < y:
    lista.append(x)
    somador = somador + 1
  print(lista)


n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

repetir(n1, n2)