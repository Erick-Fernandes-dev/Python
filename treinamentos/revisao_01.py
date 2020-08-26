lista = [9, 8, 7, 6, 7]
soma = 0 
contador = 0

while contador < 5:
  soma += lista[contador]
  contador = contador + 1
print("Média: ", (soma/contador))

'''
Criamos a lista de notas em ❶. Em ❷, criamos a estrutura de repetição para variar
o valor de x e continuar enquanto este for menor que 5. Lembre-se de que uma
lista de cinco elementos contém índices de 0 a 4. Por isso inicializamos x=0 na
linha anterior. Em ❸, adicionamos o valor de notas[0] à soma e depois notas[1],
notas[2], notas[3] e notas[4], um elemento a cada repetição. Para isso, utilizamos
o valor de x como índice e o incrementamos de 1 em ❹. Uma grande vantagem
desse programa foi que não precisamos declarar cinco variáveis para guardar as
cinco notas. Todas as notas foram armazenadas na lista, utilizando um índice
para identificar ou acessar cada valor.


'''

