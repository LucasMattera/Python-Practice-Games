nombre = str(input("Hola. ¿Cual es tu nombre? "))
edad = int(input("¿Cuántos años tenés?" ))
peso = int(input("Ok. Última pregunta: ¿cuánto pesás? "))

print("\n Si no te funcionada el Shift, tu nombre se escribiría", str(nombre).lower())
print("\n Ahora, si tuvieses el Caps Lock trabajdo, seria", str(nombre).upper())
print("\n Si un nene chiquito te quisiera llamar la atención, tu nombre se volvería:", str(nombre)*5)
print("\n Tu edad es de ", int(edad) * 365 * 24 * 60 * 60, "segundos")
print("\n ¿Sabias que en la luna pesarías solo", int(peso) / 6 , "kilos")
print("\n Ahora bien, en el Sol, tu peso sería de ", int(peso) / 27.1 , "(aunque no por mucho..)")
print(input("\n Presionar ENTER para continuar"))
