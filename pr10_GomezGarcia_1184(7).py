print(" ")
print("Andres Noe Gomez Garcia 1184: Practica 10")
print(" ")
#Define una funcion que cuenta cuántas personas tienen más de 20 años
def contar_mayores_20(edades):
    return sum(1 for edad in edades if edad > 20)

# Invoca la funcion
print(contar_mayores_20([15, 25, 30, 18, 22]))  
