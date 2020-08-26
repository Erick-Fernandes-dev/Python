def somar(lista):
  if len(lista) == 1:
    return lista[0]
  else:
    return lista[0] + somar(lista[1:])

lista = [1, 3, 5, 7, 9]
print(somar(lista))


print("CONVERTENDO PARA BINÁRIO:")

def converter(n , base):
  digitos = "01"

  if n < base:
    return digitos[n]
  
  else:
    return converter(n//base, base) + digitos[n%base]


numero = int(input("digite um valor:"))
print(converter(numero, 2))

print("CONVERTENDO PARA HEXADECIMAL:")

def convertendo(n ,base):
  digitos = "0123456789ABCDEF"

  if n < base:
    return digitos[n]
  
  else:
    return convertendo(n//base, base) + digitos[n%base]


numero_1 = int(input("Digite outro valor: "))
print(convertendo(numero_1, 16))


print("TORRE DE HANOI")

def mover_torre(altura, origem, destino, auxiliar):
  if altura >= 1:
    mover_torre(altura-1, origem, destino, auxiliar)
    print(f"movendo o disco de {origem} para {destino}")
    mover_torre(altura-1, auxiliar, destino, origem)

mover_torre(4, "A", "C", "B")
