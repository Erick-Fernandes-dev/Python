nota1 = float(input("Digite um valor: "))
nota2 = float(input("Digite mais um outro valor:"))

def media(nota1, nota2):
  soma = 21 - (nota1 + nota2)
  print("vc precisa tirar:", soma)

media(nota1, nota2)

valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite mais um outro valor: "))
valor3 = float(input("Digite um outro valor final: "))


def unidade(x, y, z):

  sm = (x + y + z)/3
  print("Sua média é:{:-2f}".format(sm))

unidade(valor1, valor2, valor3) 