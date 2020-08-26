item = open("forca.txt", "r")
print(item)
produto = open("forca.txt", "w")

produto.write("maquina")
produto.close()
print(produto)
'''
produto = open("forca.txt", "a")


for i in item:
  print(i)
def metodo_1():
  texto = item.read()
  print(texto)

def metodo_2():
  linhas = item.readlines()
  print(linhas)


metodo_1()
metodo_2()

'''
'''
linha = item.readline()

while linha != "":
  print(linha)
  linha = item.readline()

'''


