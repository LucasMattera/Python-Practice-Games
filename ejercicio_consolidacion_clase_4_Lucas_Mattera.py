"""
Se debe desarrollar un juego que, en base a una tupla de palabras predefinidas,
seleccione una y se la muestre al usuario con las letras desordenadas. 
El usuario debe adivinar cuál es la palabra.
"""
import random

print('te voy a mostrar una palabra con las letras derordenadas, vos tenes que adivinarla')

PALABRAS = ('hola', 'silla', 'pala', 'campera', 'cadena')
PALABRA_ELEGIDA = random.choice(PALABRAS)
PALABRA_ELEGIDA_LS = list(PALABRA_ELEGIDA)
random.shuffle(PALABRA_ELEGIDA_LS)
PALABRA_ELEGIDA_UNORD = ''.join(PALABRA_ELEGIDA_LS)
print(PALABRA_ELEGIDA_UNORD)
palabra_ingresada = input('adivina la palabra desordenada: ')

while palabra_ingresada.lower() != PALABRA_ELEGIDA:
	palabra_ingresada = input('\nno es la palabra, intenta de nuevo: ')

print('\nadivinaste la palabra elegida')
print(input('presiona ENTER para continuar...'))

