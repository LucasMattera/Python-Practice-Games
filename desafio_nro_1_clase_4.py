"""
1. Escribir un programa que cuenta por el usuario (mostrando los nros por pantalla). 
El usuario debe ingresar el nro inicial, el nro final, y el salto que debe llevarse a cabo.
"""

inicio = int(input('ingresa un numero DESDE el cual quieras contar: '))
final = int(input('ingresa el numero HASTA el cual quieras contar: '))
salto = int(input('ahora decime de cuanto en cuanto queres que cuente: '))

for n in range(inicio, final+1, salto):
	print(n)