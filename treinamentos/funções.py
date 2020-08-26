z = [1, 2, 3]
a = [5 ,10, 15]
b = [3, 7, 12]



def qualquer(lista):
  soma = 0

  for i in range(5):
    for numero in lista:
      soma += numero
  print(soma)

print(qualquer(z))
print(qualquer(a))
print(qualquer(b))

