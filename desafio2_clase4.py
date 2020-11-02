"""
2. Crear un programa que solicite un texto al usuario y que luego lo muestre al revés 
(utilizando sólo lo visto en clase).
"""

txt = str(input('ingrese un texto: '))
negLen = -len(txt)

for posicion in range(len(txt)):
	pos = posicion+1
	print(txt[-pos], end='')

##print(txt[-3])