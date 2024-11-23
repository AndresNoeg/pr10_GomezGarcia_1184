print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que devuelve True si el año es bisiesto
def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Invoca la funcion
print(es_bisiesto(2024)) 

