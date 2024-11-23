print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que devuelve la edad calculada a partir del año actual y el de nacimiento
def calcular_edad(actual, nacimiento):
    return actual - nacimiento

# Invoca la funcion
año_actual = 2024
personas = [("Juan", 2000), ("Ana", 1990), ("Pedro", 1985)]
for nombre, nacimiento in personas:
    print(f"{nombre} cumplirá {calcular_edad(año_actual, nacimiento)} años.")

