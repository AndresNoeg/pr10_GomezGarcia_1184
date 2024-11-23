print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que devuelve la palabra más larga de la lista
def mas_larga(lista_palabras):
    return max(lista_palabras, key=len)

# Invoca la funcion
print(mas_larga(["gato", "elefante", "perro"]))  
