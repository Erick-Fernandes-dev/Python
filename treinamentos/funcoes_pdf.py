'''def fatorial(n):
  resultado = 1

  for i in range(1, n+1):
    resultado = 1
  
  return resultado


def combinacao(p, n):
  resultado = fatorial(n)/(fatorial(p) * fatorial(n-p))

  return resultado


n1 = int(input("Digite um valor: "))
n2 = int(input("Digite mais um valor: "))

print(combinacao(n1, n2))
'''
#composição de funções

def soma(lista):
  soma = 0

  for elemento in lista:
    soma += elemento
  
  return soma


print(soma([1, 2, 4]))
my_list = [6, 8, 10]
print(soma(my_list))
print(soma([10, 20] + [30, 40]))

# Função booleana

def e_bissexto(ano):
  if(ano%4 == 0 and ano%100 != 0) or (ano%400 == 0):
    return True
  else: 
    return False


Ano = int(input("Digite algum ano: "))

if e_bissexto(Ano) == True:
  print("Fevereiro tem 29 dias")
else: 
  print("Fevereiro tem 28 dias")