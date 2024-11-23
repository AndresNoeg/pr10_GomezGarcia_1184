print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que cuenta cuántas veces aparece cada vocal en la palabra
def contar_vocales(palabra):
    vocales = "aeiou"
    return {v: palabra.lower().count(v) for v in vocales}

# Invoca la funcion
print(contar_vocales("banana"))  
