import random

print("===============================")
print("SEJA BEM VINDO AO JOGO DA FORCA")
print("===============================")

def palavra_no_txt():
  arquivo = open("new_word_forca.txt", "r") 
  lista = []
  for i in arquivo:
    lista.append(i)
  return lista

def escolher_palavra(lista):
  escolha = random.choice(lista)
  return escolha.strip()
  
def desafio(palavra_escolhida):
  lista0 = []
  for i in palavra_escolhida:
    lista0.append("_")
  return lista0


def advinhe_palavra(letra, desafio, palavra_escolhida):
  for i in range(len(palavra_escolhida)):
    if palavra_escolhida[i] == letra:
      desafio[i] = letra


palavras = palavra_no_txt()
palavra_escolhida = escolher_palavra(palavras)
palavra_desconhecida = desafio(palavra_escolhida)
numDeVidas = 6
sair = False
print(palavra_desconhecida)


while(sair == False and numDeVidas > 0):
  letra = input("Digite qual é a letra: ")
  if(letra in palavra_escolhida):
    
    advinhe_palavra(letra, palavra_desconhecida, palavra_escolhida)
    print(palavra_desconhecida)
    if(not("_" in palavra_desconhecida)):
      print("*********************************")
      print("Parabénsssss!!! Você conseguiu!!!")
      print("*********************************")
      sair = True
  
  else: 
    numDeVidas -= 1
    print("==============================")
    print("Que pena!!!!!, Você errou!!!")
    print("==============================")
  if(numDeVidas == 0):
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("!Você já errou 6 vezes!!!, Portanto, você foi enforcado!!!")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    
    print("-------------------")
    print("Programa terminado.")
    print("-------------------")

