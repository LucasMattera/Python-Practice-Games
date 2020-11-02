"""
• Modificar el juego de adivinar el número para que tenga una cantidad de intentos limitada. Si se falla esa cantidad de veces
, el programa debe terminar indicando cuál era el numero, junto con la correspondiente, 
esperable y apropiada frase de burla *emoji de carita*
"""

import random

bienvenida = input(
	'\n- Hola, a continuacion tenes que adivinar el nro entre uno y cien que piense yo. \nPresiona ENTER para comenzar..')
nro = random.randint(1, 4)
limiteDeIntentos = 5
intentos = 0
nroIngresado = int(input('- ingresa el numero \n\t'))

while (nroIngresado != nro) and (intentos < limiteDeIntentos):
	intentos += 1
	print('- ya llevas', intentos, 'intentos')
	print('- te quedan', limiteDeIntentos-intentos, 'intentos\n')
	if nroIngresado > nro:
		nroIngresado = int(input('- elegite un numero mas bajo:\n\t '))
	elif (limiteDeIntentos-intentos) == 1:
		print('un ultimo intento de yapa')
	else: 
		nroIngresado = int(input('- elegite un numero mas alto:\n\t '))

if intentos == limiteDeIntentos:
	print('fallaste, te quedaste sin intentos')
	print('el numero era', nro, 'lero lero!')
elif nroIngresado == nro:
	print('\n- exelente, adivinaste el numero, era ', nro, '\n- te ha tomado ', intentos, 'intentos adivinarlo')

input('\nENTER para terminar..')


