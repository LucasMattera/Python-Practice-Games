
import random

bienvenida = input(
	'\n- Hola, a continuacion tenes que adivinar el nro entre uno y cien que piense yo. \nPresiona ENTER para comenzar..')
nro = random.randint(1, 2)
intentos = 0
nroIngresado = int(input('- ingresa el numero \n\t'))

while nroIngresado != nro:
	intentos += 1
	print('- ya llevas', intentos, 'intentos\n')
	if nroIngresado > nro:
		nroIngresado = int(input('- elegite un numero mas bajo:\n\t '))
	else: 
		nroIngresado = int(input('- elegite un numero mas alto:\n\t '))

print(
	'\n- exelente, adivinaste el numero, era ', nro, '\n- te ha tomado ', intentos, 'intentos adivinarlo')

input('\nENTER para terminar..')
