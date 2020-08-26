# Variáveis globais
tiposDeNotas = [5, 10, 20, 50, 100]
totalNoCaixa = [0]
quantTotalDeNotas = [0]
quantDeCadaNota = []


'''
Inicializa a quatidade de cada nota com '0'
Ex:
quantDeCadaNota = [0, 0, 0, 0 ,0]
Logo temos:
0 notas de 5
0 notas de 10
0 notas de 20
0 notas de 50
0 notas de 100
'''


def insereValoresIniciais(lista):
    for i in range(len(tiposDeNotas)):
        lista.append(0)


# Verifica se é unidade
def unidade(valor):
    if valor >= 0 and valor <= 9:
        return True
    else:
        return False


# Verifica se é dezena
def dezena(valor):
    if valor >= 10 and valor <= 99:
        return True
    else:
        return False


# Verifica se é centena
def centena(valor):
    if valor >= 100 and valor <= 999:
        return True
    else:
        return False


# Classifica a ordem do valor passado
def ordemDoValor(valor):
    if unidade(valor):
        return 1
    elif dezena(valor):
        return 2
    elif centena(valor):
        return 3
    else:
        return 0


# Calcula o total de dinheiro no caixa
def calculaQuantTotalNoCaixa():
    for i in range(len(quantDeCadaNota)):
        totalNoCaixa[0] += tiposDeNotas[i] * quantDeCadaNota[i]


# Calcula a quantidade total de notas
def calculaQuantTotalDeNotas():
    for i in range(len(quantDeCadaNota)):
        quantTotalDeNotas[0] += quantDeCadaNota[i]


# Carregar o caixa
def carregarCaixa():
    for i in range(len(tiposDeNotas)):
        quantDeCadaNota[i] = int(
            input(f'Quantas notas de R${tiposDeNotas[i]},00: '))
    calculaQuantTotalNoCaixa()
    calculaQuantTotalDeNotas()


# Saca o dinheiro do caixa
def sacarDinheiro(valor):
    saqueTotal = []
    insereValoresIniciais(saqueTotal)
    if (valor <= totalNoCaixa[0]):
        # Se o valor para sacar é igual alguma nota, atualizo a quantidade e retorno o valor
        if (tiposDeNotas.count(valor) == 1):
            i = tiposDeNotas.index(valor)
            if (quantDeCadaNota[i] > 0):
                quantDeCadaNota[i] -= 1
                saqueTotal[i] = 1
                return saqueTotal

        ordem = ordemDoValor(valor)
        if(ordem == 1):
            quantDeCadaNota[0] -= 1
            saqueTotal[0] = 1
            return saqueTotal
        elif (ordem == 2):
            
            if (valor > 10 and valor < 20):
                if (valor > 20 and valor < 50):
                    if (valor > 50 and valor < 100):

        elif (ordem == 3):
        else:

    else:
        return False


# def calculaSaque()


# Imprime as opções (menu)
def opcoes():
    print('\n')
    print('===== OPÇÕES =====')
    print('(1) Carregar caixa eletrônico')
    print('(2) Sacar dinheiro')
    print('(3) Sair')


# Retorna a escolha do usuário
def escolha():
    opcao = input('\nDigite a opção: ')
    return opcao


# Menu do programa
def menu():
    insereValoresIniciais(quantDeCadaNota)
    opcao = ''
    sair = False

    while(sair != True):
        opcoes()
        opcao = escolha()
        if(opcao == '1'):
            carregarCaixa()
        elif(opcao == '2'):
            valor = int(input('Valor do saque: '))
            saqueTotal = sacarDinheiro(valor)
            if(saqueTotal):
                print('Operação efetuada com sucesso!')
                for i in range(saqueTotal):
                    total = 0
                    print(f'{saqueTotal[i]} de R${tiposDeNotas[i]},00')
                    total += tiposDeNotas[i]
                print(f'Valor total sacado: {total}')
            elif(saqueTotal == False):
                print(
                    f'O caixa não possui saldo suficiente para sacar R${valor},00')
            print(quantDeCadaNota)
        elif(opcao == '3'):
            sair = True
        else:
            print('Opção inválida!')


# Executa o programa
menu()


# outra forma de fazer o 'if' em 'sacarDinheiro()'

# for i in range(len(tiposDeNotas)):
#     if (valor == tiposDeNotas[i] and quantDeCadaNota[i] > 0):
#         quantDeCadaNota[i] -= 1
#         saqueTotal[i] = 1
#         return saqueTotal
