print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que devuelve las palabras con más de n caracteres
def filtrar_palabras(lista_palabras, n):
    return [palabra for palabra in lista_palabras if len(palabra) > n]

# Invoca la funcion
print(filtrar_palabras(["gato", "elefante", "perro"], 4)) 
