var = int(input("Digite um valor: "))
var2 = float(input("Digite outro valor: "))
var3 = float(input("Digite um outro valor: "))
var4 = float(input("Digite mais um ultimo valor: "))
name = input("Digite seu primeiro nome: ")
name2 = input("Digite seu segundo nome: ")

media = (var + var2 + var3 + var4) // 4
concatencao = name + name2

if media >=7:
  print("você está aprovado",  concatencao)
elif media == 6:
  print("você está na final",   concatencao)
elif media <= 5:
  print("você está reprovado",  concatencao)

print(media)
print(concatencao)

print("="*30)

numero = int(input("Digite um valor: "))
contador = 0

while contador <= numero:
  print(contador)
  contador = contador + 1

numero2 = int(input("Digite um valor: "))
contador2 = 0

while contador2 <= numero2:
  x = int(input("Digite mais um outro valor: "))
  contador2 = contador2 + x
  contador2 += 1

print(contador2)