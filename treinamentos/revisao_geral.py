print("Revisão Geral")

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

print("Seja bem vindo", nome, sobrenome)

casa = input("Está limpa ou suja: ")

if casa == 'suja':
  print("vá arrumar a casa!!")
else :
  print("Faça outra tarefa.")

sexto_de_lixo = input("Verifique se está vazio ou cheio: ")

from time import sleep

if sexto_de_lixo == "cheio":
  print("Leve o lixo para o latão, ande uns 10 passos.")
  contador = 0
  while contador <= 10:
    print(contador)
    contador = contador + 1
    sleep(1)
  print("Parabéns você chegou ao seu destino.")
else: 
  print("Procure outra tarefa.")