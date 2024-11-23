print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que cuenta las letras mayúsculas en la cadena
def contar_mayusculas(cadena):
    return sum(1 for char in cadena if char.isupper())

# Invoca la funcion
print(contar_mayusculas("Hola Mundo"))  
