print("="*40)
print(f"{:^40}SEJA BEM VINDO(A) AO CAIXA ELETRÔNICO.")
print("="*40)


tipos_de_notas = [5, 10, 20, 50, 100]
total_no_caixa = [0]
quant_total_de_notas = [0]
quant_de_cada_nota = []

def insereValoresIniciais(lista):
  for i in range(len(tipos_de_notas)):
    lista.append(0)

def unidade(valor):
  if valor >= 0 and valor <= 9:
    return True 
  else:
    return False


def dezena(valor):
  if valor >= 10 and valor <= 99:
    return True
  else:
    return False


def centena(valor):
  if valor >= 100 and valor <= 999:
    return True
  else:
    return False

def ordem_do_valor(valor):
  if unidade(valor):
    return 1
  elif dezena(valor):
    return 2
  elif centena(valor):
    return 3
  else:
    return 0


def calcula_quant_total_no_caixa():
  for i in range(len(quant_de_cada_nota)):
    total_no_caixa[0] += tipos_de_notas[i] * quant_de_cada_nota[i]


def calcula_quant_total_de_notas():
  for i in range(len(quant_de_cada_nota)):
    quant_total_de_notas[0] += quant_de_cada_nota[i]


def carregar_caixa():
  for i in range(len(tipos_de_notas)):
    quant_de_cada_nota[i] = int(input(f"Quantas notas de R${tipos_de_notas[1]},00: "))
    calcula_quant_total_no_caixa()
    calcula_quant_total_de_notas()


def sacar_dinheiro(valor):
  saque_total = []
  insere_valores_iniciais(saquetotal)
  if (valor <= total_no_caixa[0]):
    if(tipos_de_notas.count(valor) == 1):
      i = tipos_de_notas.index(valor)
      if (quant_de_cada_nota[i] > 0):
        quant_de_cada_nota[i] -= 1
        saque_total[1] = 1
        return saque_total

    ordem = ordem_do_valor(valor)
    elif(ordem == 1):
      quant_de_cada_nota[0] -= 1
      saque_total[0] = 1
      return saque_total
    elif (ordem == 2):
      if (valor > 10 and valor < 20):
      
      elif (valor > 20 and valor < 50):
      elif (valor > 50 and valor < 100):
    
    elif (ordem == 3):
    else:

  else:
    return False


def opcoes():
  print("\n")
  print("======== Opções ========")
  print("(1)-Carregar caixa eletrônico")
  print("(2)-Sacar dinheiro")
  print("(3)-Sair")


def escolha():
  opcao = input("\nEscolha Alguma dessas opções: ")
  return opcao


def menu():
  insere_valores_iniciais(quant_de_cada_nota)
  opcao = ""
  sair = False

  while (sair != True):
    opcoes()
    opcao = escolha()
    if (opcao == "1"):
      carregar_caixa()
    elif (opcao == "2"):
      valor = int(input("Valor do saque: "))
      saque_total = sacar_dinheiro(valor)
      if (saque_total):
        print("Opreção efetuada com sucesso!!!")
        for i in range(saque_total):
          total = 0
          print(f"{saque_total[i]} de R${tipos_de_notas[i]},00")
          total += tipos_de_notas[i]
        print(f"Valor total sacado: {total}")
      elif (saque_total == False):
        print(f"O caixa não possui saldo suficiente pra sacar R${valor},00")
      print(quant_de_cada_nota)
    elif (opcao == "3"):
      sair = True 
    else:
      print("~"*30)
      print(f"{:^30}Opção inválida!!")
      print("~"*30)


menu()


