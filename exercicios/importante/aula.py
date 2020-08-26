continuar = True

while continuar:
    op = input("DDigite o operador: ")
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite um outro valor: "))

    if op == '+':
        print(n1+n2)
        resposta = str.upper(input("Deseja continuar, digite (s) para 'sim' e (n) para 'não': "))
        if  resposta != "S":
            continuar = False
    elif op == '-':
        print(n1-n2)
        resposta = str.upper(input("Deseja continuar, digite (s) para 'sim' e (n) para 'não': "))
        if  resposta != "S":
            continuar = False
    elif op == '*':
        print(n1*n2)
        resposta = str.upper(input("Deseja continuar, digite (s) para 'sim' e (n) para 'não': "))
        if  resposta != "S":
            continuar = False

    elif op == '/':
        print(n1/n2)
        resposta = str.upper(input("Deseja continuar, digite (s) para 'sim' e (n) para 'não': "))
        if  resposta != "S":
            continuar = False
  
