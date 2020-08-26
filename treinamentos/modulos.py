import arquivos_modulos
import math
import random
import os

'''
EXISTEM DIFERENTES FORMAS DE IMPORTAR:

from arquivos_modulos import soma
from arquivos_modulos import soma, diferenca
from arquivos_modulos import soma as s
from arquivos_modulos import soma as s, diferenca as d

'''
Resultado = arquivos_modulos.soma([7, 8, 9], [4, 6, 8])
print(Resultado)


lista_dif = arquivos_modulos.diferenca([1, 2, 3], [5, 7, 9])
print(lista_dif)

print(math.pi)
print(math.factorial(5))
print(math.radians(90))

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))

lista = [1, 2, 3, 4]
random.shuffle(lista)
print(lista)

print(os.getcwd())
#print(os.uname())
print(os.listdir())
print(os.system("dir"))