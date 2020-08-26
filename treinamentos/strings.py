#STRINGS
#ITERANDO STRINGS

'''nome = "erick fernandes"
print(nome[0])

for i in nome:
  print(i)

'''
nome_2 = "yamazaki"
indice = 0

while indice < len(nome_2):
  print(nome_2[indice])
  indice += 1
'''
def contador():
  string = "estudar"
  cont = 0
  while (cont < len(string)):
    print(string[indice]).count("a")
    cont = cont + 1

contador()'''
'''
valor = 30
desconto = 0.1

print(f"o produto custava{valor}, mas com desconto fica {30*(1-desconto)}")

nome = "erick"
idade = 20

print(f"{nome} tem {idade} anos")

lista = [9, 8, 7]

print(f"o tamanho da lista é {len(lista)}")

pi = 3.14159265358979323846
print(f"pi: {pi: 2f}")

#especificando o tamanho mínimo que o número vai ocupar 

outro = 123.456789
print(f"{pi:5.2f}")
print(f"{outro:5.2f}")

alunos = ["amanda", "erick", "daniel", "marcos"]

for aluno in alunos:
  print(f"{aluno:>9}")

for aluno in alunos:
  print(f"{aluno:<9}")

for aluno in alunos:
  print(f"{aluno:^9}")

n = 300
print(f"{n:x}")
print(f"{n:o}")
print(f"{n:e}")

n1 = 0.25

print(f"{n1:%}")
print(f"{n1:.2%}")
print(f"{n1:10.2f}")
'''

print("RETIRAR LETRAS:")

def retirar_vogais(texto):
  resultado = ''

  for c in texto:
    if c not in "aeiou":
      resultado += c
  return resultado


texto = input("Digite alguma palavra: ")
print(retirar_vogais(texto))

